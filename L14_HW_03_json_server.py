import requests

reply = requests.get('http://localhost:3000')

if reply.status_code == requests.codes.ok:
    print("ALL RIGHT!")
else:
    print("BAD!")

print(reply.status_code)
print(reply.headers)
print(reply.headers['Content-Type'])

print()
print(requests.codes.__dict__)

print()
print(reply.text)
