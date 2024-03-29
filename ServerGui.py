from PyQt5 import QtWidgets
from PyQt5.Qt import QMainWindow, QTableWidgetItem, QFileDialog, QInputDialog, QLineEdit, QMessageBox, QListWidgetItem

from PyQt5.QtCore import Qt, QThread

import psutil
import os
from util import Server, JsonHandler
from util.workers import CpuWorker, GuiWorker, RamWorker
from UiFiles import Ui_ServerGui

"""TODO
- Implement the custom arguments field on the startup page
- Take into account the min ram and max ram values from the startup page on startup
- Implement new class to handle the server options list widgets
- Update the server options list widgets with real information 
- Name the server options line edits appropriately and take their input into account
- Implement general file editor
- Re-Consider the concept behind the json loader class and why it shouldnt just be handled by ServerGui 
- Attempt remote connection support with support in the data file to salt and hash the login details
- Implement error logging page
- Re-visit the calculation for getting maximum possible ram that can be allocated 
- Re-visit system for scrolling console 
- Implement ran commands into Server to allow use of the up arrow to get last command
"""

showed_server_options_warning = False


class ServerGui(QMainWindow, Ui_ServerGui):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.start_button.clicked.connect(self.start_server)
        self.execute_button.clicked.connect(self.execute_command)
        self.restart_button.clicked.connect(self.restart_server)
        self.reload_button.clicked.connect(self.reload_server)
        self.kill_button.clicked.connect(self.kill_server)
        self.listWidget.set_window(self)
        self.max_ram = round(psutil.virtual_memory().total / 1000 / 1000 - 1000)
        self.qt_threads = []

        self.max_ram_label.setText('Max. Ram: %sMB' % str(self.max_ram))
        self.json = JsonHandler()
        self.server = Server()
        self.min_ram_label.setText('Min. Ram: 0MB')
        self.max_ram_slider.setMaximum(self.max_ram)
        self.min_ram_slider.setMaximum(self.max_ram)

        java_versions = []
        for folder in os.listdir("C:/Program Files/Java"):
            if folder.startswith('jre'):
                java_versions.append(folder)

        self.java_version_combo_box.addItems(sorted(java_versions))
        self.java_version_combo_box.setCurrentIndex(
            self.java_version_combo_box.findText(self.json.last_server['java-version']))
        self.java_version_combo_box.currentTextChanged.connect(self.java_version_selected)

        self.min_ram_slider.valueChanged.connect(self.min_slider_moving)
        self.max_ram_slider.valueChanged.connect(self.max_slider_moving)
        self.create_server_config_button.clicked.connect(self.create_server_configuration)
        self.max_ram_slider.setValue(self.json.last_server['max-ram'])
        self.min_ram_slider.setValue(self.json.last_server['min-ram'])
        self.current_config_combo_box.addItems(self.json.servers().keys())
        self.current_config_combo_box.setCurrentIndex(
            self.current_config_combo_box.findText(self.json.current_server()))
        self.current_config_combo_box.currentTextChanged.connect(self.set_server)
        self.launch_server_button.clicked.connect(self.start_server)
        self.add_whitelist_button.clicked.connect(self.add_player_to_whitelist)

        self.jar_file_line_edit.setText(self.json.get_directory()["full-path"][0])

        header = self.tableWidget.horizontalHeader()
        for i in range(0, 5):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        header = self.server_options_table.horizontalHeader()
        for i in range(0, 3):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.server_options_table.verticalHeader().setVisible(False)
        self.splitter.setSizes([100, 600])
        self.server_options_table.itemChanged.connect(self.update_server_options)
        self.server_options_table.itemDoubleClicked.connect(self.show_edit_warning)
        self.setup_server_options()

        self.cpu_worker = CpuWorker()
        self.cpu_worker_thread = QThread()
        self.cpu_worker.intReady.connect(self.cpu_value_ready)
        self.cpu_worker.moveToThread(self.cpu_worker_thread)
        self.cpu_worker_thread.started.connect(self.cpu_worker.procCounter)
        self.cpu_worker_thread.start()
        self.qt_threads.append(self.cpu_worker_thread)

        self.ram_worker = RamWorker()
        self.ram_worker_thread = QThread()
        self.ram_worker.intReady.connect(self.ram_value_ready)
        self.ram_worker.moveToThread(self.ram_worker_thread)
        self.ram_worker_thread.started.connect(self.ram_worker.procCounter)
        self.ram_worker_thread.start()
        self.qt_threads.append(self.ram_worker_thread)

        self.gui_worker = GuiWorker()
        self.gui_worker_thread = QThread()
        self.gui_worker.intReady.connect(self.gui_value_ready)
        self.gui_worker.moveToThread(self.gui_worker_thread)
        self.gui_worker_thread.started.connect(self.gui_worker.procCounter)
        self.gui_worker_thread.start()
        self.qt_threads.append(self.gui_worker_thread)

        self.server.set_window(self)

    def add_player_to_whitelist(self):
        if self.add_whitelist_line_edit.text() == '':
            return
        if self.json.add_player_to_whitelist(self.add_whitelist_line_edit.text()):
            self.whitelist_list_widget.clear()
            self.setup_whitelisted_players_widget()
            self.add_whitelist_line_edit.setText('')

    def update_server_options(self, item):
        if self.loading_server_options:
            return
        key = self.server_options_table.item(item.row(), 0).text()
        item = item.text()
        directory_dict = self.json.get_directory()
        path = directory_dict['working-directory'] + '/server.properties'
        lines = [line.strip() for line in open(path, 'r')]
        for index, line in enumerate(lines):
            if line.startswith('#'):
                continue
            split_line = line.split('=')
            if split_line[0] == key:
                lines[index] = "%s=%s" % (key, item)
        with open(path, 'w') as f:
            for line in lines:
                f.write(line + '\n')
            f.close()

    def show_edit_warning(self):
        global showed_server_options_warning
        if not showed_server_options_warning and self.server.isAlive():
            QMessageBox.about(self, 'Python Server Gui Dialog',
                              'You are about to modify a server option, these changes will not take affect until the server is restarted.')
            showed_server_options_warning = True

    def set_server(self):
        if self.server.isAlive():
            self.server.stop_server()
            self.server = Server()
            self.start_button.setText('Start')
        self.json.set_server(self.current_config_combo_box.currentText())
        self.min_ram_slider.setValue(self.json.last_server['min-ram'])
        self.max_ram_slider.setValue(self.json.last_server['max-ram'])
        self.java_version_combo_box.setCurrentText(self.json.last_server['java-version'])
        self.jar_file_line_edit.setText(self.json.last_server['jar-file'])
        self.server_options_table.setRowCount(0)
        self.clear_server_options()
        self.setup_server_options()

    def clear_server_options(self):
        self.ops_list_widget.clear()
        self.banned_ips_list_widget.clear()
        self.banned_players_list_widget.clear()

    def setup_server_options(self):
        self.loading_server_options = True
        directory_dict = self.json.get_directory()
        path = directory_dict['working-directory'] + '/server.properties'
        if not os.path.exists(path):
            self.server_options_table.setRowCount(0)
            return
        lines = [line.strip() for line in open(directory_dict['working-directory'] + '/server.properties', 'r') if
                 not line.startswith('#') and line != '']
        self.server_options_table.setRowCount(len(lines))
        row = 0
        column = 0
        for line in lines:
            key, value = line.split('=')
            if column == 2:
                column = 0
                row += 1
            if column == 0:
                item = QTableWidgetItem(key)
                item.setFlags(Qt.ItemIsEnabled)
                self.server_options_table.setItem(row, column, item)
                column += 1
            self.server_options_table.setItem(row, column, QTableWidgetItem(value))
            column += 1
        self.setup_whitelisted_players_widget()
        self.setup_banned_players_widget()
        self.setup_banned_ips()
        self.setup_operators()
        self.loading_server_options = False

    def setup_whitelisted_players_widget(self):
        whitelisted_players = self.json.whitelisted_players()
        if whitelisted_players is None:
            return
        for player in whitelisted_players:
            self.whitelist_list_widget.addItem(QListWidgetItem(player['name']))

    def setup_operators(self):
        operators = self.json.operators()
        if operators is None:
            return
        for player in operators:
            self.ops_list_widget.addItem(QListWidgetItem(player['name']))

    def setup_banned_players_widget(self):
        banned_players = self.json.banned_players()
        if banned_players is None:
            return
        for player in banned_players:
            self.banned_players_list_widget.addItem(QListWidgetItem(player['name']))

    def setup_banned_ips(self):
        banned_ips = self.json.banned_ips()
        if banned_ips is None:
            return
        for ip in banned_ips:
            self.banned_ips_list_widget.addItem(QListWidgetItem(str(ip['ip'])))

    def java_version_selected(self):
        self.json.set_java_version(self.java_version_combo_box.currentText())

    def cpu_value_ready(self, i):
        vbar = self.scrollArea.verticalScrollBar()
        vbar.setValue(vbar.maximum())
        self.cpu_progress_bar.setValue(i)

    def ram_value_ready(self, i):
        self.ram_progress_bar.setValue(i)

    def gui_value_ready(self, i):
        self.gui_usage_progress_bar.setValue(i)

    def min_slider_moving(self):
        self.min_ram_label.setText("Min Ram: %sMB" % str(self.min_ram_slider.value()))
        self.json.set_min_ram(self.min_ram_slider.value())
        if self.min_ram_slider.value() >= self.max_ram_slider.value():
            self.max_ram_slider.setValue(self.min_ram_slider.value())
            self.max_ram_slider.update()

    def max_slider_moving(self):
        self.max_ram_label.setText("Max Ram: %sMB" % str(self.max_ram_slider.value()))
        self.json.set_max_ram(self.max_ram_slider.value())
        if self.max_ram_slider.value() <= self.min_ram_slider.value():
            self.min_ram_slider.setValue(self.max_ram_slider.value())

    def update_players(self):
        for i in range(0, self.tableWidget.rowCount()):
            self.tableWidget.removeRow(i)
        self.tableWidget.setRowCount(len(self.server.get_players()))

        row = 0
        column = 0
        for player in self.server.get_players():
            for item in player.values():
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1
            row += 1
            column = 0

    def closeEvent(self, e):
        if self.server.isAlive():
            self.server.stop_server()
        for thread in self.qt_threads:
            thread.quit()

    def keyPressEvent(self, e):
        key = e.key()
        if key == Qt.Key_Enter or key == Qt.Key_Return:
            self.execute_command()
        elif key == Qt.Key_Up:
            if len(ran_commands) == 0:
                return
            self.input_lineedit.setText(ran_commands[-1])

    def start_server(self):
        text = self.start_button.text()
        if text == 'Start':
            directory_dict = self.json.get_directory()
            path = directory_dict['full-path']
            if ' ' in path[0]:
                path[0] = "\"" + path[0] + "\""
            self.server.set_directory(directory_dict['working-directory'])
            self.server.set_args(path)
            self.server.set_window(self)

            self.server.start()
            self.start_button.setText('Stop')
        elif text == "Stop":
            self.server.stop_server()
            self.server = Server()
            self.start_button.setText('Start')

    def execute_command(self):
        if not self.server.isAlive():
            self.input_lineedit.setText('')
            return
        self.execute_input(self.input_lineedit.text())

    def execute_input(self, input):
        if not self.server.isAlive():
            return
        self.server.execute_input(input)
        self.input_lineedit.setText('')

    def restart_server(self):
        if not self.server.isAlive():
            return
        self.server.stop_server()
        self.server = Server()
        self.start_button.setText('Start')
        self.start_server()

    def reload_server(self):
        if not self.server.isAlive():
            return
        self.server.execute_input('reload')
        self.server.execute_input('reload confirm')

    def kill_server(self):
        if not self.server.isAlive():
            return
        self.server.stop_server()
        self.server = Server()
        self.start_button.setText('Start')

    def create_server_configuration(self):
        name = QInputDialog.getText(self, 'Python Server Gui Dialog',
                                    'Please give this new server configuration a name', QLineEdit.Normal)[0]
        if name == '':
            return
        jar_file = QFileDialog.getOpenFileName(self, 'Select Jar File', '', 'JAR File (*.jar)')[0]
        if jar_file == '':
            return
        file = '\\'.join(jar_file.split('/'))
        min_ram = 0
        max_ram = 0
        server = {
            "min-ram": min_ram,
            "max-ram": max_ram,
            "java-version": self.java_version_combo_box.currentText(),
            "jar-file": file,
            "custom-arguments": None
        }
        self.max_ram_slider.setValue(0)
        self.min_ram_slider.setValue(0)
        self.json.create_server(name, server)
        self.current_config_combo_box.clear
        self.current_config_combo_box.addItems(self.json.servers().keys())
        self.current_config_combo_box.setCurrentIndex(self.current_config_combo_box.findText(name))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ServerGui()
    window.show()
    sys.exit(app.exec_())
