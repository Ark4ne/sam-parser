class Header:
    def __init__(self):
        self.__header = {}

    def push(self, name, values):
        self.__header[name] = {}

        for value in values:
            if not str(value).startswith('@'):
                parts = str(value).split(':', maxsplit=1)
                self.__header[name][parts[0]] = parts[1]

    def len(self):
        return len(self.__header)

    def get_sn(self):
        if '@SQ' in self.__header and 'SN' in self.__header['@SQ']:
            return self.__header['@SQ']['SN']

        return None

    def print(self):
        for section, values in self.__header.items():
            print("===== " + section + " =====")
            for name, value in values.items():
                print('-- ' + name + ' : ' + value)
