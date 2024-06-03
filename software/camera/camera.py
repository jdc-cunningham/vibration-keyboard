import time

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import CircularOutput

# referenced modular pi cam project
class Camera:
  def __init__(self):
    self.picam2 = None
    self.recording = False
    self.video_config = self.picam2.create_video_configuration(main={"size": (1680, 660), "format": "YUV420"})
    self.encoder = H264Encoder(30000000, repeat=True)
    self.encoder.output = CircularOutput(buffersize = 150)
  
  def setup(self):
    self.picam2 = Picamera2()
    self.picam2.switch_mode(self.video_config)
  
  def start_recording(self):
    if (self.recording): return

    filename = str(time.time()) + '.h264'
    self.encoder.output.fileoutput = filename
    self.encoder.output.start()
    self.recording = True

  def stop_recording(self):
    if (not self.recording): return

    self.encoder.output.stop()
    self.picam2.stop_encoder()
    self.recording = False
