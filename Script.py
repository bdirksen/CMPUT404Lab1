import requests

url = "https://raw.githubusercontent.com/bdirksen/CMPUT404Lab1/main/Script.py"
r = requests.get(url)
print(r.text)