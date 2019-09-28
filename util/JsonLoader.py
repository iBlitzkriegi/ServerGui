import json


class JsonHandler:
    def __init__(self):
        with open('data.json', 'r') as file:
            self.data = json.load(file)
            file.close()

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
        print(self.data['servers'][last_server])
        return self.data['last-server']
