import requests
from urllib.parse import urlencode

url = "https://baconipsum.com/api/" + "?" + urlencode({"type": "all-meat"}) + "&" + urlencode({"sentences": 3})
response = requests.get(url)
print()
