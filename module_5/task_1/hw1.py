import os


class KeyValueStorage:
    def __init__(self, path_to_file: str):
        self.path_to_file = path_to_file
        self.data = self.parse_data()
        self.add_attributes()

    def parse_data(self):
        result = {}
        with open(self.path_to_file, 'r') as file_to_parse:
            for line in file_to_parse.readlines():
                key = line.split('=')[0]
                value = line.split('=')[1]
                result[key] = self.parse_int_if_possible(value)
        return result

    def __getitem__(self, key):
        return self.data[key]

    def add_attributes(self):
        for key, value in self.data.items():
            setattr(self, key, value)

    @staticmethod
    def parse_int_if_possible(value_to_parse):
        try:
            return int(value_to_parse)
        except ValueError:
            return value_to_parse


if __name__ == "__main__":
    storage = KeyValueStorage(os.getcwd() + "\\task1.txt")
    print(f"{storage['name']} its type: {type(storage['name'])}")
    print(f"{storage.name} its type: {type(storage.name)}")
    print(f"{storage.last_name} its type: {type(storage.last_name)}")
    print(f"{storage.power} its type: {type(storage.power)}")
    print(f"{storage.song} its type: {type(storage.song)}")
    print(f"{storage['power']} its type: {type(storage['power'])}")

# name=kek
# last_name=top
# power=9001
# song=shadilay
