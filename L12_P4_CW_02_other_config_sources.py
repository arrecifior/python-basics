import configparser

config = configparser.ConfigParser()

dict = {
    'DEFAULT': {
        'host': 'localhost'
    },
    'mariadb': {
        'name': 'hello',
        'user': 'root',
        'password': 'password'
    },
    'redis': {
        'port': 6379,
        'db': 0
    }
}

print(config.read(dict))

print('Sections:', config.sections(),'\n')

print('mariadb section:')
print('Host:', config['mariadb']['host'],)
print('Database:', config['mariadb']['name'],)
print('Username:', config['mariadb']['user'],)
print('Password:', config['mariadb']['password'], '\n')

print('redis section:')
print('Host:', config['redis']['host'],)
print('Port:', config['redis']['port'],)
print('Database number:', config['redis']['db'],)