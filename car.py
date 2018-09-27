#coding:utf-8
from datetime import datetime, timedelta, timezone
import requests
import json

apikey = ''
url = 'http://webservice.recruit.co.jp/carsensor/usedcar/v1/?key=' + apikey + '&format=json&pref=11,13&person=7&model=ヴァンガード'

response = requests.get(url)
data = json.loads(response.text)
num =  data["results"]["results_returned"]

JST = timezone(timedelta(hours=+9), 'JST')
now = datetime.now(JST).strftime("%Y-%m-%d %H:%M")

f = open('car.txt', 'a')
f.write('---------------' + now + '---------------\n' + num  + '台\n\n')
f.close()

num = int(num)

for i in range(num):
  model = data["results"]["usedcar"][i]["model"]
  year = str(data["results"]["usedcar"][i]["year"])
  color = data["results"]["usedcar"][i]["color"]
  inspection = data["results"]["usedcar"][i]["inspection"]
  odd = data["results"]["usedcar"][i]["odd"]
  price = str(data["results"]["usedcar"][i]["price"])

  f = open('car.txt', 'a')
  f.write(model + '\n' + year + '\n' + color + '\n' + inspection + '\n' + odd + '\n' + price + '\n\n')
  f.close()

print('取得完了')
