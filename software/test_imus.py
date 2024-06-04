import time

from imu.imu import Imu

# human POV (looking at device)
imu_left = Imu(0)
imu_right = Imu(1)

imu_left.start()
imu_right.start()

left_val = 0
right_val = 0

while (True):
  il_val = imu_left.accel[2]
  ir_val = imu_right.accel[2]

  if (left_val == 0):
    left_val = il_val

  if (right_val == 0):
    right_val = ir_val
    continue

  il_diff = il_val - left_val
  ir_diff = ir_val - right_val

  print(il_diff, ir_diff)

  left_val = il_val
  right_val = ir_val

  time.sleep(0.1)
