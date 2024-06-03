import time

from threading import Thread
from imu.imu import Imu
from led.led import Led
from camera.camera import Camera

# human POV (looking at device)
imu_left = Imu(0)
imu_right = Imu(1)
status_led = Led()
cam = Camera()

imu_left.start()
imu_right.start()

time.sleep(3)
open('data.txt', 'w').close() # empty
text_file = open('data.txt', 'a')
Thread(target=cam.start_recording).start()
status_led.turn_on()

stop = False

def record_data():
  while not stop:
    text_file.write(str(imu_left.accel[2]) + ',' + str(imu_right.accel[2]) + ' | ')
    time.sleep(0.1)

Thread(target=record_data).start()

time.sleep(2)

stop = True
text_file.close()
cam.stop_recording()
status_led.turn_off()
