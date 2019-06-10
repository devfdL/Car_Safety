import android
import math
import time

droid = android.Android()
droid.startLocating(5000, 30)
interval = 10

# earth radius = 6371km
rad = 6371

def getGPS():
    locs = droid.getLastKnownLocation()
    gpspos = locs.result["gps"]
    if gpspos != None:
        lat = gpspos["latitude"]
        lon = gpspos["longitude"]
        t = gpspos["time"]
        return [lat, lon, t]
    return None

def deg2rad(deg):
    return deg * (math.pi/180)

def calcDistance(p0, p1):
    dlat = deg2rad(p0[0] - p1[0])
    dlon = deg2rad(p0[1] - p1[1])
    a = math.sin(dlat/2)*math.sin(dlat/2) + math.cos(deg2rad(p0[0]))*math.cos(deg2rad(p1[0])) *math.sin(dlon/2)*math.sin(dlon/2)
    c = 2*math.atan2(math.sqrt(a),math.sqrt(1-a))
    return rad*c

def compareGPS(p0, p1):
    return p0[0] == p1[0] and p0[1] == p1[1]   

pos0 = None
while pos0 == None:
    pos0 = getGPS()

while True:
    time.sleep(interval)

    pos1 = getGPS()
    
    if pos1 != None and compareGPS(pos0,pos1) == False:
        d = calcDistance(pos0,pos1)
        t = (pos1[2]-pos0[2])/1000

        print(str(d)+"km in "+str(t)+"s"+" - "+str(d*(60/t)*60)+"kph")
        pos0 = pos1[:]

droid.stopLocating()
