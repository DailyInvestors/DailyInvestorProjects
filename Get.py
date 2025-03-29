import requests

url = "https://www.example.com"
response = requests.get(url)

if response.status_code == 200:
    print(f"Request successful! Status code: {response.status_code}")
    print(response.text) 
else:
    print(f"Request failed. Status code: {response.status_code}")

