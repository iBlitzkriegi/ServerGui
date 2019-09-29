import json


class JsonHandler:
    def __init__(self):
        with open('data.json', 'r') as file:
            self.data = json.load(file)
            file.close()
        last_server = self.data['last-server']
        self.last_server = self.data['servers'][last_server]

    def update_key(self, key, new_dictionary):
        self.data[key] = new_dictionary

    def dump_data(self):
        with open('data.json', 'w') as file:
            json.dump(self.data, file, indent=4)
            file.close()

    def last_server(self, input=None):
        if input is not None:
            self.data['last-server'] = input
            self.dump_data()
            return
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

