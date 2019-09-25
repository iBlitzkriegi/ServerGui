import html
import json
import requests


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

    def get_uuid_from_name(self, player_name):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36'}
        page = requests.get('https://mcuuid.net/?q=' + player_name, headers=headers)
        doc = html.fromstring(page.content)
        xpath_full_uuid = '/html/body/div/div[2]/ul/li/div/div[2]/table/tbody/tr[1]/td[2]/input/@value'
        raw_uuid = doc.xpath(xpath_full_uuid)
        uuid = ''.join(raw_uuid)
        return uuid if uuid != '' else None
