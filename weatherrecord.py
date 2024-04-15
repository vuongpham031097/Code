# IMPORT THƯ VIỆN
import datetime as dt
import requests

print("CHÀO MỪNG ĐẾN VỚI TRUNG TÂM DỰ BÁO KHÍ TƯỢNG THỦY VĂN TRUNG ƯƠNG")
# KHAI BÁO URL GỐC ĐỂ ĐỂ CALLING API
# CẤU TRÚC BASE_URL api.openweathermap.org/data/2.5/onecall? 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "7fbcba29db10295dffe5ba34f8b24d55"

# KHAI BÁO BIẾN THÀNH PHỐ ĐỂ NHẬP
CITY = input("Vui Lòng Nhập Thành Phố Của Bạn : ")

# ĐỔI ĐỘ K THÀNH ĐỘ C
def kelvin_to_celsius(kelvin):
    DoC = kelvin - 273.15
    return DoC

# CALLING API
url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

# LẤY TỌA ĐỘ ĐỊA ĐIỂM
City_Lon = response['coord']['lon']
City_Lat = response['coord']['lat']

# LẤY DỮ LIỆU NHIỆT ĐỘ VÀ CHUYỂN THÀNH ĐỘ C
temp_kelvin = response['main']['temp']
temp_DoC = kelvin_to_celsius(temp_kelvin)

# LẤY TỐC ĐỘ GIÓ
wind_speed = response['wind']['speed']

# LẤY ĐỘ ẨM
humidity = response['main']['humidity']

# LẤY GIỜ MẶT TRỜI MỌC VÀ LẶN
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

# IN DỮ LIỆU VỪA LẤY VỀ
print(f"Kinh Độ : {City_Lon}")
print(f"Vĩ Độ : {City_Lat}")
print(f"Nhiệt Độ Tại Lều Khí Tượng : {temp_DoC:.2f}°C")
print(f"Độ Ẩm : {humidity:.2f}%")
print(f"Tốc Độ Gió Trung Bình : {wind_speed:.2f}m/s")
print(f"Mặt Trời Mọc Lúc : {sunrise_time} giờ địa phương")
print(f"Mặt Trời Lặn Lúc : {sunset_time} giờ địa phương")