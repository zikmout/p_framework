class Config:
    ''' bla bla '''
    path = 'C:\\Users\\zak\\Projects'
    def __init__(self, name, fmt):
        self.name = name
        self.fmt = fmt
        self.project_path = Config.path + name + '\\' + name + '.json'
        self._load_config()

    def _load_config():
        print('Enter Load project')
        with open(self.project_path) as json_data_file:
            project_file = json.load(json_data_file)
        self.toto = project_file['Data']['toto']
        self.toto1 = project_file['Data']['toto1']
    
    def print_config(self):
        print(self.name)
        print(self.fmt)
        print(self.toto)
        print(self.toto1)
