import threading
from subprocess import Popen, PIPE
from util.PlayerChecks import PlayerChecks
import datetime

directory = "C:\\Python\\Scripts\\ServerGui\\TestingServer\\"
player_checks = PlayerChecks(directory)


class Server(threading.Thread):

    def __init__(self, dir=None, *args, **kwards):
        super().__init__()
        self._stop = threading.Event()
        self.directory = dir
        self.args = args
        self.process = None
        self.running = False
        self.players = []

    def set_directory(self, directory):
        if self.stopped is False:
            self.stop_server()
        self.directory = directory

    def stop_server(self):
        if self.stopped is False:
            return
        self.execute_input("stop")
        self.args = None
        self.directory = None

    def set_args(self, *args):
        if self.stopped is False:
            self.stop_server()
        self.args = args

    def set_window(self, window):
        self.window = window

    def execute_input(self, input):
        new_input = 'say ' + input + '\n' if self.window.say_checkbox.isChecked() else input + '\n'
        if input == 'stop':
            self.window.start_button.setText('Start')
        byte_input = new_input.encode('utf-8')
        self.process.stdin.write(byte_input)
        self.process.stdin.flush()
        # ran_commands.append(input)
        self.window.input_lineedit.setText('')

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

    def is_living(self):
        return self.living

    def get_players(self):
        return self.players

    def run(self):
        self.process = Popen(['java', '-jar'] + list(self.args), cwd=self.directory, stderr=PIPE, stdout=PIPE,
                             stdin=PIPE)
        vbar = self.window.scrollArea.verticalScrollBar()
        self.running = True
        while self.process.poll() is None:
            if self.stopped():
                return
            line = self.process.stdout.readline()
            try:
                utf_line = line.decode('utf-8').strip()
            except UnicodeDecodeError:
                continue
            if utf_line != '':
                output = line.rstrip()
                print(output.decode('utf-8'))
                self.window.output_label.setText(self.window.output_label.text() + '\n' + output.decode('utf-8'))
                vbar.setValue(vbar.maximum())

                if 'logged in' in utf_line:
                    information = utf_line.split(' ')
                    player = information[2]
                    name = player.split('[')[0]
                    ip = player.split('/')[1].replace(']', '')
                    current_time = datetime.datetime.now()
                    player_dict = {
                        "name": name,
                        "ip": ip,
                        "time-joined": current_time.strftime('%I:%M %p'),
                        "whitelisted": player_checks.is_whitelisted(name),
                        "op": player_checks.is_op(name)
                    }
                    self.players.append(player_dict)
                    self.window.listWidget.add_player(player_dict)
                    self.window.update_players()
                elif 'left the game' in utf_line or 'Disconnected' in utf_line:
                    information = utf_line.split(' ')
                    name = information[2]
                    for index, player in enumerate(self.players):
                        if player['name'] == name:
                            self.players.pop(index)
                            self.window.listWidget.remove_player_by_index(index)
                    self.window.update_players()
        self.process = None
        for i in range(0, self.window.tableWidget.rowCount()):
            self.window.tableWidget.removeRow(i)
        self.window.listWidget.clear()
        self.process = None
        self.players.clear()
