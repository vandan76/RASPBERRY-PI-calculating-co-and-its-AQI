from mq import *
import sys, time

try:
    print("Press CTRL+C to abort.")
    
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
        else :
             sys.stdout.write("AQI: reading is too much high")
        sys.stdout.flush()
        time.sleep(0.1)
except:
    print("\nAbort by user")

