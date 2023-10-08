
import sys
import requests

print(sys.version)
# print(sys.executable)


def greet(who_to_greet):
    greeting = f'Hello, {who_to_greet}'
    return greeting


r = requests.get('https://google.com', timeout=100)
print(r.status_code)

print(greet('Santi'))
