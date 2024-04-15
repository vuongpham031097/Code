import datetime
import requests

Date = datetime.date.today()
Money = input("Nhập tiền tệ muốn quy đổi : ")
Money_change = input("Nhập tiền tệ muốn quy đổi sang :")
Amount = input("Nhập số lượng muốn quy đổi: ")

Base_url = "https://api.apilayer.com/exchangerates_data/convert?"

url = Base_url + "to=" + Money_change + "&from=" + Money + "&amount=" + Amount + "&date=" + str(Date)

payload = {}
headers = {
    "apikey": "0C2xiBwOyDHQJyoqzRhAF9gP9ocRE7U8"
}

response = requests.request("GET", url, headers=headers, data=payload)

result = response.text

print(result)