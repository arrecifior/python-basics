import configparser

config = configparser.ConfigParser()
config.read('configNew.ini')

config['redis']['db'] = '123'

with open('configNew.ini', 'w') as configfile:
    config.write(configfile)
