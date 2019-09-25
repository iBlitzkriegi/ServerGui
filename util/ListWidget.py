from PyQt5.Qt import QListWidget, QMenu, QAction, QIcon, QListWidgetItem
import os

path = os.path.dirname(os.path.realpath(__file__)) + '\\'


class ListItem(QListWidgetItem):
    def __init__(self, player, parent=None):
        global path
        QListWidgetItem.__init__(self, parent)
        self.setText(player)
        self.setIcon(QIcon(path + "head.png"))


class ListWidget(QListWidget):
    def __init__(self, icon, parent=None):
        QListWidget.__init__(self, parent)
        self.setUniformItemSizes(True)
        self.head_icon = icon
        self.players = []
        global path
        self.path = path

    def set_window(self, window):
        self.window = window

    def add_item(self, player_name):
        item = QListWidgetItem()
        item.setText(player_name)
        item.setIcon(self.get_icon('head.png'))
        self.addItem(item)

    def add_player(self, player_dictionary):
        self.players.append(player_dictionary)
        self.update_players()

    def update_players(self):
        self.clear()
        for player in self.players:
            self.add_item(player['name'])

    def remove_player_by_name(self, player_name):
        for index, player in enumerate(self.players):
            if player['name'] == player_name:
                self.players.pop(index)
                self.update_players()
                print('FDEAD')

    def remove_player_by_index(self, index):
        if len(self.players) == 0:
            return
        self.players.pop(index)
        self.update_players()

    def get_icon(self, file_name):
        return QIcon(self.path + file_name)

    def contextMenuEvent(self, e):
        if self.selectionModel().selection().indexes():
            for i in self.selectionModel().selection().indexes():
                row, column = i.row(), i.column()
            player_name = self.window.listWidget.selectedItems()[0].text()
            menu = QMenu(self)

            op_action = QAction("Op", self.window)
            op_action.setIcon(self.get_icon('head.png'))
            menu.addAction(op_action)

            deop_action = QAction('De-Op', self)
            deop_action.setIcon(self.get_icon('head.png'))
            menu.addAction(deop_action)

            kick_action = QAction("Kick", self)
            kick_action.setIcon(self.get_icon('head.png'))
            menu.addAction(kick_action)

            ban_action = QAction("Ban", self)
            ban_action.setIcon(self.get_icon('head.png'))
            menu.addAction(ban_action)

            gamemode = menu.addMenu('Gamemode')
            gamemode.setIcon(self.get_icon('head.png'))
            gamemode.addAction('Creative')
            gamemode.addAction('Survival')
            gamemode.addAction('Adventure')

            action = menu.exec_(self.mapToGlobal(e.pos()))
            if action is None:
                return
            action = action.text()
            if "Kick" in action or "Ban" in action:
                print(self.players)
                for index, player in enumerate(self.players):
                    print(player)
                    if player['name'] == player_name:
                        self.remove_player_by_index(index)
                if "Kick" in action:
                    self.window.execute_input("kick " + player_name)
                else:
                    self.window.execute_input("ban " + player_name)

                self.window.update_players()
            elif "Op" == action:
                self.window.execute_input("op " + player_name)
                ##TODO Update players op dict value maybe?
            elif "De-Op" in action:
                self.window.execute_input("deop " + player_name)
            elif "Survival" in action:
                self.window.execute_input("gamemode survival " + player_name)
            elif "Creative" in action:
                self.window.execute_input("gamemode creative " + player_name)
            elif "Adventure" in action:
                self.window.execute_input("gamemode adventure " + player_name)
