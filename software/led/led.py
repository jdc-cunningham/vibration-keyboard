import RPi.GPIO as GPIO

class Led:
  def __init__(self):
    self.on = False
    self.pin = 4

    self.setup()

  def setup(self):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(self.pin, GPIO.OUT)

  def turn_on(self):
    if (self.on): return

    GPIO.output(self.pin, GPIO.HIGH)
    self.on = True

  def turn_off(self):
    if (self.on): return

    GPIO.output(self.pin, GPIO.LOW)
    self.on = False