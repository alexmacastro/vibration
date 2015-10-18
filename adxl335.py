#!/usr/bin/python

from serial import Serial
import re
import time

serial_pattern = r"(.?\d+\.\d*)\n";
serial_port = '/dev/ttyUSB0';
serial_bauds = 9600;

ts = time.time()

def main():

  print "Opening serial port"
  s = Serial(serial_port, serial_bauds);
  print "Reading first line from port"
  line = s.readline()
  print "Initializing communication"
  counter = 1
  # debug stuff
  # tic = time.time()
  log = open("/home/pi/vibration/log.csv", "a")

  while counter <= 1000:
    counter += 1
    line = s.readline()
    m = re.match(serial_pattern, line)
    try:
      log.write("\n" +  str(ts) + "," + str(counter) + "," + str(m.group(1)))
    except:
      log.write("\n" +  str(ts) + "," + str(counter) + "," + str("NaN"))

  # debug stuff
  # toc = time.time()
  # print(tic)
  # print(toc)
  log.close()

if __name__ == "__main__":
  main()
