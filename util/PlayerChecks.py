import json


class PlayerChecks:
    def __init__(self, directory):
        self.directory = directory

    def is_whitelisted(self, player_name):
        with open(self.directory + 'whitelist.json', 'r') as f:
            whitelist = json.load(f)
            f.flush()
            f.close()
        player = [player for player in whitelist if player['name'] == player_name]
        return len(player) != 0

    def is_op(self, player_name):
        with open(self.directory + 'ops.json', 'r') as f:
            operators = json.load(f)
            f.flush()
            f.close()
        player = [player for player in operators if player['name'] == player_name]
        return len(player) != 0
