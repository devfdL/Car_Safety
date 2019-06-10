from gps import *
import time
import threading
import math
import RPi.GPIO as GPIO ## Import GPIO library
import time ## Import 'time' library. Allows us to use 'sleep'

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering
GPIO.setup(40,GPIO.OUT) ## Setup GPIO Pin 40 to OUT

class GpsController(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            # grab EACH set of gpsd info to clear the buffer
            self.gpsd.next()

    def stopController(self):
        self.running = False

    @property
    def fix(self):
        return self.gpsd.fix

    @property
    def utc(self):
        return self.gpsd.utc

    @property
    def satellites(self):
        return self.gpsd.satellites

mph = 15

if __name__ == '__main__':
    # create the controller
    gpsc = GpsController() 
    try:
        # start controller
        gpsc.start()
        while True:
            time.sleep(1)
            if gpsc.fix.speed < mph :
                #print("speed is under 15 mph",gpsc.fix.speed)
                #print(mph)
                GPIO.output(40,GPIO.HIGH)
                time.sleep(1)
                GPIO.output(40,GPIO.LOW)
                time.sleep(1)


            elif gpsc.fix.speed > mph :
                print("speed (m/s) ",gpsc.fix.speed)
                #    GPIO.cleanup()

            else:
                print("fine")
                
            time.sleep(1)

#Error
    #except:
    #   print "Unexpected error:", sys.exc_info()[0]
    #  raise

    #Ctrl C
    except KeyboardInterrupt:
        print("User cancelled")

    finally:
        print("Stopping gps controller")
        gpsc.stopController()
        #wait for the thread to finish
        gpsc.join()

    print("Done")

GPIO.cleanup()
