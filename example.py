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
        if perc["co"] <=4.4:
        ans=((50-0)/(4.4-0))*(perc["co"]-0)+0

        elif 4.4>perc["co"] and 9.5>perc["co"]:
            ans=((100-51)/(9.4-4.5))*(perc["co"]-4.5)+51

        elif 9.4>perc["co"] and 12.5>perc["co"]:
            ans=((150-101)/(12.4-9.5))*(perc["co"]-9.5)+101

        elif 12.4>perc["co"] and 15.5>perc["co"]:
            ans=((200-151)/(15.4-12.5))*(perc["co"]-12.5)+151

        elif 15.4>perc["co"] and 30.5>perc["co"]:
            ans=((300-201)/(30.4-15.5))*(perc["co"]-15.5)+201

        elif 30.4>perc["co"] and 40.5>perc["co"]:
            ans=((400-301)/(40.5-30.5))*(perc["co"]-30.5)+301

        elif 40.4>perc["co"] and 50.5>perc["co"]:
            ans=((500-401)*(50.5-40.5))(perc["co"]-40.5)+401
        sys.stdout.write("AQI:",ans)
        sys.stdout.flush()
        time.sleep(0.1)

except:
    print("\nAbort by user")
