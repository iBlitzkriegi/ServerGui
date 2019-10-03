import json
import os
import requests
import lxml.html


class JsonHandler:
    def __init__(self):
        with open('data.json', 'r') as file:
            self.data = json.load(file)
            file.close()
        last_server = self.data['last-server']
        self.last_server = self.data['servers'][last_server]

    def servers(self):
        return self.data['servers']

    def add_player_to_whitelist(self, player_name):
        uuid_of_player = self.get_uuid_from_name(player_name)
        if uuid_of_player is None:
            return False
        directory = self.last_server['jar-file']
        path = ''.join([dirt + "/" for dirt in directory.split('\\') if '.jar' not in dirt])
        if not os.path.exists(path + 'whitelist.json'):
            return False
        with open(path + 'whitelist.json', 'r') as f:
            whitelisted_players = json.load(f)
            f.close()

        whitelisted_players.append({
            "uuid": uuid_of_player,
            "name": player_name
        })
        with open(path + 'whitelist.json', 'w') as f:
            json.dump(whitelisted_players, f, indent=4)
            f.close()
        return True

    ##TODO MAKE THIS REPEATED PATH LINE JUST A CLASS FIELD??

    def whitelisted_players(self):
        directory = self.last_server['jar-file']
        path = ''.join([dirt + "/" for dirt in directory.split('\\') if '.jar' not in dirt])
        if not os.path.exists(path + 'whitelist.json'):
            return None
        with open(path + 'whitelist.json', 'r') as f:
            whitelisted_players = json.load(f)
            f.close()
        return whitelisted_players

    def banned_players(self):
        directory = self.last_server['jar-file']
        path = ''.join([dirt + "/" for dirt in directory.split('\\') if '.jar' not in dirt])
        if not os.path.exists(path + 'banned-players.json'):
            return None
        with open(path + 'banned-players.json', 'r') as f:
            banned_players = json.load(f)
            f.close()
        return banned_players

    def banned_ips(self):
        directory = self.last_server['jar-file']
        path = ''.join([dirt + "/" for dirt in directory.split('\\') if '.jar' not in dirt])
        if not os.path.exists(path + 'banned-ips.json'):
            return None
        with open(path + 'banned-ips.json', 'r') as f:
            banned_ips = json.load(f)
            f.close()
        return banned_ips

    def operators(self):
        directory = self.last_server['jar-file']
        path = ''.join([dirt + "/" for dirt in directory.split('\\') if '.jar' not in dirt])
        if not os.path.exists(path + 'ops.json'):
            return None
        with open(path + 'ops.json', 'r') as f:
            operators = json.load(f)
            f.close()
        return operators

    def create_server(self, name, new_server):
        self.data['last-server'] = name
        self.data['servers'][name] = new_server
        self.dump_data()
        self.last_server = self.data['servers'][name]

    def current_server(self):
        return self.data['last-server']

    def dump_data(self):
        with open('data.json', 'w') as file:
            json.dump(self.data, file, indent=4)
            file.close()

    def set_server(self, server):
        self.data['last-server'] = server
        self.last_server = self.data['servers'][server]
        self.dump_data()
        return

    def last_server(self):
        last_server = self.data['last-server']
        return self.data['servers'][last_server]

    def set_min_ram(self, ram):
        self.last_server['min-ram'] = ram
        self.dump_data()

    def set_max_ram(self, ram):
        self.last_server['max-ram'] = ram
        self.dump_data()

    def set_java_version(self, java_version):
        self.last_server['java-version'] = java_version
        self.dump_data()

    def set_jar_file(self, path):
        self.last_server['jar-file'] = path
        self.dump_data()

    def set_arguments(self, *args):
        self.last_server['custom-arguments'] = args
        self.dump_data()

    def get_directory(self):
        directory = self.last_server['jar-file']
        path = ''.join([dirt + "/" for dirt in directory.split('\\') if '.jar' not in dirt])
        data = {
            "working-directory": path,
            "full-path": [directory]
        }
        return data

    def get_uuid_from_name(self, player_name):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.85 Safari/537.36'}
        page = requests.get('https://mcuuid.net/?q=' + player_name, headers=headers)
        doc = lxml.html.fromstring(page.content)
        xpath_full_uuid = '/html/body/div/div/ul/li/div/div[2]/table/tbody/tr[1]/td[2]/input/@value'
        raw_uuid = doc.xpath(xpath_full_uuid)
        uuid = ''.join(raw_uuid)
        return uuid if uuid != '' else None
