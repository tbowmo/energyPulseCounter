#!/usr/bin/python
import serial
import urllib2
import os.path
import syslog

#Configuration bits
domoticz = "http://localhost:8080"
sensorIdx = "17" # This must be a string, for later concatenation!

# The measCacheFile is written with the count from the sensor,
# this is so that we can seed the sensor with the previous counter value,
# and continue from that point of.
measCacheFile = "/var/spool/pulseCount/meascache.txt"

#Configure the right serialport for arduino below!
ser = serial.Serial('/dev/ttyACM0',115200,timeout=None)

if not os.path.exists(os.path.dirname(measCacheFile)):
    os.makedirs(os.path.dirname(measCacheFile))
    
#Read the file, and output it on serial (if it exists!)
if (os.path.isfile(measCacheFile)):
  f = open(measCacheFile, 'r')
  x = f.readline()
  ser.write(x)
  ser.write("\n")
  
syslog.syslog('pulseCount started')

while 1:
  try:
    line = ser.readline()
  except Exception, e:
    syslog.syslog(syslog.LOG_ERR, "Failed to read serial ")
    continue
  x = line.split(";")
  url = domoticz+"/json.htm?type=command&param=udevice&idx="+sensorIdx+"&nvalue=0&svalue="+x[0]+";"+x[1]
  try :
    urllib2.urlopen(url).read()
  except urllib2.URLError, e:
    syslog.syslog(syslog.LOG_ERR, "error = " + str(e.reason))
    
  t = open(measCacheFile, 'w')
  t.truncate()
  t.write(x[1])
  t.write("\n")
  t.close()
    
ser.close()
