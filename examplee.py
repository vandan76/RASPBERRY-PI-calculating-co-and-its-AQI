
import example
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
lcd1 = 12
lcd2 = 7
lcd3 = 21
lcd4 = 25
lcd5 = 24
lcd6 = 23

lcd = LCD.Adafruit_charLCD(lcd1 ,lcd2 ,lcd3 ,lcd4 ,lcd5 ,lcd6, 0, 16, 2)

while True :
    x=test.ans
    y=test.perc["CO"]
    lcd.clear()
    lcd.message("co value: " + str(y) + "\nAQI OF CO iS: " + str(x))
    time.sleep(1)



