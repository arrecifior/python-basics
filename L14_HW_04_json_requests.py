import requests

try:
    reply = requests.get('http://localhost:3000', timeout=1)
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t get your data')
else:
    print('Here is your data, my Master!')


try:
    reply = requests.get('https://vk.com', timeout=0.0000001)
except requests.exceptions.Timeout:
    print('Sorry, Mr. Impatient, you didn\'t det your data')
else:
    print('Here is your data, my Master!')


try:
    reply = requests.get('http://localhost:3001', timeout=1)
except requests.exceptions.ConnectionError:
    print("Nobody's home, sorry!")
else:
    print('Everythind\'s fine!')

try:
    reply = requests.get('http://///////')
except requests.exceptions.InvalidURL:
    print('Recipient unknown!')
else:
    print('Everything fine!')
