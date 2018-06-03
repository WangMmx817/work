# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:49:29 2018
#引用其他工具包
import 包名/类名
@author: lenovo
"""

import urllib.request as r
city_pinyin=input("请输入城市拼音：")
address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
print(info)

#json(dict)格式工具包
import json
data=json.loads(info)
wendu=data['main']['temp']
print("温度:"+str(wendu))
zuidi=data['main']['temp_min']
print("最低温度:"+str(zuidi))
zuigao=data['main']['temp_max']
print("最高温度:"+str(zuigao))
qiya=data['main']['pressure']
print("气压:"+str(qiya))
shidu=data['main']['humidity']
print("湿度:"+str(shidu))
qingkuang=data['weather'][0]['description']
print("天气情况:"+str(qingkuang))

