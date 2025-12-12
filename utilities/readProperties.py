import configparser
import os

config = configparser.RawConfigParser()
config_path = os.path.join(os.path.abspath(os.curdir), "configs", "config.ini")
config.read(config_path)

class ReadConfig:

    @staticmethod
    def getApplicationURL():
        url = config.get('commonInfo','baseURL')
        return url
    
    @staticmethod
    def getUseremail():
        username = config.get('commonInfo','email')
        return username
    
    @staticmethod
    def getpassword():
        password = config.get('commonInfo','password')
        return password
    
  