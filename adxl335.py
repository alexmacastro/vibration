from serial import Serial
import re
import urllib

serial_pattern = r"VibX: (\d+\.\d*)\n";
serial_port = '/dev/ttyUSB0';
serial_bauds = 9600;


def open_serial_port() :
  s = Serial(serial_port, serial_bauds);
  line = s.readline();
  return s

def read_temperature(s):
  line = s.readline();
  m = re.match(serial_pattern, line);
  return float(m.group(1))


if __name__ == "__main__":
  print "Opening serial port"
  s = Serial(serial_port, serial_bauds);
  print "Reading first line from port"
  line = s.readline();
  print "Initializing communication"
  while 1:
    line = s.readline()
    m = re.match(serial_pattern, line);
    vib= m.group(l)

