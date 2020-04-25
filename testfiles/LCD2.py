
import time

import Adafruit_CharLCD as LCD

import requests

url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"lat":"0","units":"%22imperial%22","mode":"xml%2C html","q":"Alliston"}


# Raspberry Pi pin configuration:
lcd_rs        = 7  # Note this might need to be changed to 21 for older revision Pi's.
lcd_en        = 8
lcd_d4        = 25
lcd_d5        = 24
lcd_d6        = 23
lcd_d7        = 18
lcd_backlight = 1

lcd_columns = 16
lcd_rows    = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7,
                           lcd_columns, lcd_rows, lcd_backlight)

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "bf8145af8emsh882cbe4cee55ea9p114679jsn9a97d316c12c"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
format_add = responce['temp']

print(format_add)

lcd.message('EXA\nCORP')

while True:
	lcd.set_backlight(0)
	time.sleep(0.5)
	lcd.set_backlight(1)
	time.sleep(0.5)


