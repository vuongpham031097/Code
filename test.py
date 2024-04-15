import requests

url = "https://api.apilayer.com/exchangerates_data/convert?to=VND&from=USD&amount=1"

payload = {}
headers= {
  "apikey": "0C2xiBwOyDHQJyoqzRhAF9gP9ocRE7U8"
}

response = requests.get(url, headers=headers)

result = response.text

print(result)