from mq import *
import sys, time
import Adafruit_CharLCD  as LCD
import RPi.GPIO as GPIO

try:
    print("Press CTRL+C to abort.")
    GPIO.setmode(GPIO.BCM)
    
    lcd1 = 12 
    lcd2 = 7
    lcd3 = 21
    lcd4 = 25
    lcd5 = 24
    lcd6 = 23

    lcd = LCD.Adafruit_CharLCD(lcd1, lcd2, lcd3, lcd4, lcd5, lcd6, 0, 16, 2)
    
    mq = MQ();
    while True:
        perc = mq.MQPercentage()
        sys.stdout.write("\r")
        sys.stdout.write("\033[K")
        sys.stdout.write("CO: %g ppm" % (perc["CO"]))
        if perc["CO"] <=4.4:
            ans=((50-0)/(4.4-0))*(perc["CO"]-0)+0
            sys.stdout.write("AQI: %g" % ans)
        elif 4.4>perc["CO"] and 9.5>perc["CO"]:
            ans=((100-51)/(9.4-4.5))*(perc["CO"]-4.5)+51
            sys.stdout.write("AQI: %g" % ans)
        elif 9.4>perc["CO"] and 12.5>perc["CO"]:
            ans=((150-101)/(12.4-9.5))*(perc["CO"]-9.5)+101
            sys.stdout.write("AQI: %g" % ans)
        elif 12.4>perc["CO"] and 15.5>perc["CO"]:
            ans=((200-151)/(15.4-12.5))*(perc["CO"]-12.5)+151
            sys.stdout.write("AQI: %g" % ans)
        elif 15.4>perc["CO"] and 30.5>perc["CO"]:
            ans=((300-201)/(30.4-15.5))*(perc["CO"]-15.5)+201
            sys.stdout.write("AQI: %g" % ans)
        elif 30.4>perc["CO"] and 40.5>perc["CO"]:
            ans=((400-301)/(40.5-30.5))*(perc["CO"]-30.5)+301
            sys.stdout.write("AQI: %g" % ans)
        elif 40.4>perc["CO"] and 50.5>perc["CO"]:
            ans=((500-401)*(50.5-40.5))(perc["CO"]-40.5)+401
            sys.stdout.write("AQI: %g" % ans)
        sys.stdout.flush()
  
       x=ans
       y=perc["CO"]
       lcd.clear()
       lcd.message("co value: " + str(y) + "\nAQI OF CO iS: " + str(x))
       time.sleep(1)
except:
    print("\nAbort by user")
