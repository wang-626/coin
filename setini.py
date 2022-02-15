import os 
import configparser
class ini():
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.proDir = os.path.split(os.path.realpath(__file__))[0]#切割 123/456/789.py 切割成 [0]123/456[1]789.py   #返回path的真實路徑  

    def ini_set(self): 
        self.configPath = os.path.join(self.proDir, "set.ini")
        if os.path.exists(self.configPath):
            pass
        else:
            self.config['coin'] = {'coin1': 'BTC','coin2': 'ETH','coin3': 'BNB','coin4': 'ADA','coin5': 'LUNA'}
            os.chdir(self.proDir) #改變path
            with open('set.ini', 'w') as configfile: #建立ini檔
                 self.config.write(configfile) 
       
    def ini_read(self):
        self.config.read(self.configPath)
        return self.config['coin']

    def ini_change(self,x1,x2,x3,x4,x5):
        self.config['coin']['coin1'] = x1
        self.config['coin']['coin2'] = x2
        self.config['coin']['coin3'] = x3
        self.config['coin']['coin4'] = x4
        self.config['coin']['coin5'] = x5

        with open('set.ini', 'w') as configfile: #建立ini檔
                self.config.write(configfile)