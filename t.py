import requests

get_user = requests.get("http://localhost:5000/user/?id=8")
print(get_user.json())
