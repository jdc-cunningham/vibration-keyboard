import time

from imu.imu import Imu

# human POV (looking at device)
imu_left = Imu(0)
imu_right = Imu(1)

while (True):
  print('left ' + str(imu_left.accel[2]))
  print('right ' + str(imu_left.accel[2]))
  time.sleep(0.1)
