import requests

x = requests.delete('https://w3schools.com/python/demopage.php')

print(x.text)