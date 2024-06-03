import time

from imu.imu import Imu
from led.led import Led

# human POV (looking at device)
imu_left = Imu(0)
imu_right = Imu(1)
status_led = Led()

imu_left.start()
imu_right.start()

status_led.turn_on()
time.sleep(1)
status_led.turn_off()

while (True):
  print('left ' + str(imu_left.accel[2]))
  print('right ' + str(imu_right.accel[2]))
  time.sleep(0.1)
