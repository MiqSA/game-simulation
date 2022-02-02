from app.main.services.config_print import bcolors
import json, os



def check_if_path_exist(path):
    try:
        if os.path.exists(path):
            return True
        else:
            return False
    except:
        print('Error in locate file')





class JsonFiles:
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

    def manager(self, mode, data=None):
        with open(f'{self.path}{self.filename}', mode) as file:
            if mode == 'r':
                return json.load(file)
            else:
                json.dump(data, file)


    def new(self, data=None):
        try:
            if check_if_path_exist(self.path) is False:
                os.makedirs(self.path)
            self.manager('w', data)
        except Exception as err:
            print(f"{bcolors.WARNING} Error Dont created new file! {bcolors.ENDC}", err)


    def read(self):
        try:
            data = self.manager('r')
            return data
        except Exception as err:
            return False


    def update(self):
        pass

    def clear(self):
        self.manager('w', data={})