import time

from imu.imu import Imu

# human POV (looking at device)
imu_left = Imu(69)
imu_right = Imu(68)

while (True):
  print('left ' + imu_left.accel[2])
  print('right ' + imu_left.accel[2])
  time.sleep(0.1)
