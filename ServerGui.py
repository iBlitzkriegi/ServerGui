from PyQt5 import QtWidgets
from PyQt5.Qt import QMainWindow, QTableWidgetItem

from PyQt5.QtCore import Qt, QThread

import psutil
import os
from util import PlayerChecks, Server
from util.workers import CpuWorker, GuiWorker, RamWorker
from UiFiles import Ui_ServerGui


args = ['C:\\Python\\Scripts\\ServerGui\\TestingServer\\paperclip.jar']
directory = "C:\\Python\\Scripts\\ServerGui\\TestingServer\\"

max_ram = round(psutil.virtual_memory().total / 1000 / 1000 - 1000)
qt_threads = []

process = []
ran_commands = []
server_dead = True


class ServerGui(QMainWindow, Ui_ServerGui):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        self.start_button.clicked.connect(self.start_server)
        self.execute_button.clicked.connect(self.execute_command)
        self.restart_button.clicked.connect(self.restart_server)
        self.reload_button.clicked.connect(self.reload_server)
        self.kill_button.clicked.connect(self.kill_server)
        self.listWidget.set_window(self)

        global max_ram
        global qt_threads
        """TODO
        MAKE THESE SET TO THE SERIALIZED DATA
        """
        self.max_ram_label.setText('Max. Ram: ' + str(max_ram) + "MB")
        self.min_ram_label.setText('Min. Ram: 0MB')
        self.max_ram_slider.setMaximum(max_ram)
        self.min_ram_slider.setMaximum(max_ram)

        java_versions = []
        for folder in os.listdir("C:/Program Files/Java"):
            if folder.startswith('jre'):
                java_versions.append(folder)
        self.java_version_combo_box.addItems(sorted(java_versions))

        self.min_ram_slider.valueChanged.connect(self.min_slider_moving)
        self.max_ram_slider.valueChanged.connect(self.max_slider_moving)

        header = self.tableWidget.horizontalHeader()
        for i in range(0, 5):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.splitter.setSizes([100, 600])

        self.cpu_worker = CpuWorker()
        self.cpu_worker_thread = QThread()
        self.cpu_worker.intReady.connect(self.cpu_value_ready)
        self.cpu_worker.moveToThread(self.cpu_worker_thread)
        self.cpu_worker_thread.started.connect(self.cpu_worker.procCounter)
        self.cpu_worker_thread.start()
        qt_threads.append(self.cpu_worker_thread)

        self.ram_worker = RamWorker()
        self.ram_worker_thread = QThread()
        self.ram_worker.intReady.connect(self.ram_value_ready)
        self.ram_worker.moveToThread(self.ram_worker_thread)
        self.ram_worker_thread.started.connect(self.ram_worker.procCounter)
        self.ram_worker_thread.start()
        qt_threads.append(self.ram_worker_thread)

        self.gui_worker = GuiWorker()
        self.gui_worker_thread = QThread()
        self.gui_worker.intReady.connect(self.gui_value_ready)
        self.gui_worker.moveToThread(self.gui_worker_thread)
        self.gui_worker_thread.started.connect(self.gui_worker.procCounter)
        self.gui_worker_thread.start()
        qt_threads.append(self.gui_worker_thread)
        self.server = Server()
        self.server.set_window(self)

    def cpu_value_ready(self, i):
        vbar = self.scrollArea.verticalScrollBar()
        vbar.setValue(vbar.maximum())
        self.cpu_progress_bar.setValue(i)

    def ram_value_ready(self, i):
        self.ram_progress_bar.setValue(i)

    def gui_value_ready(self, i):
        self.gui_usage_progress_bar.setValue(i)

    def min_slider_moving(self):
        self.min_ram_label.setText("Min Ram: " + str(self.min_ram_slider.value()) + "MB")
        if self.min_ram_slider.value() >= self.max_ram_slider.value():
            self.max_ram_slider.setValue(self.min_ram_slider.value())
            self.max_ram_slider.update()

    def max_slider_moving(self):
        self.max_ram_label.setText("Max Ram: " + str(self.max_ram_slider.value()) + "MB")
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
        ##TODO
        global server_dead
        global qt_threads
        if not server_dead:
            global process
            process.stdin.write(b'stop\n')
            process.stdin.flush()
        for thread in qt_threads:
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
        print('clo')
        text = self.start_button.text()
        global directory
        global args
        if text == 'Start':
            print('STARTY')
            self.server.set_directory(directory)
            print('[[')
            self.server.set_args(args)
            self.server.set_window(self)
            self.server.start()
            self.start_button.setText('Stop')
        elif text == "Stop":
            print('stop')
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
        global directory
        global args
        self.server.stop_server()
        self.server = Server()
        print('STARTING NEW')
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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = ServerGui()
    window.show()
    sys.exit(app.exec_())