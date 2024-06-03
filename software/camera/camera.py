import time, os

from picamera2 import Picamera2
from picamera2.encoders import H264Encoder, Quality
from picamera2.outputs import CircularOutput

# referenced modular pi cam project
class Camera:
  def __init__(self):
    self.picam2 = Picamera2()
    self.recording = False
    self.video_config = self.picam2.create_video_configuration(main = {"size": (1680, 660), "format": "RGB888"})
    self.encoder = H264Encoder(30000000, repeat = True)
    self.encoder.output = CircularOutput(buffersize = 150)
    self.video_filename = None

    self.setup()
  
  def setup(self):
    self.picam2.configure(self.video_config)
    self.picam2.start()
  
  def start_recording(self):
    if (self.recording): return

    self.video_filename = str(time.time()) + '.h264'
    self.picam2.start_encoder(self.encoder)
    self.picam2.set_controls({"FrameRate": 30})
    self.encoder.output.fileoutput = self.video_filename
    self.encoder.output.start()
    self.recording = True

    while self.recording:
      if (not self.recording):
        return

      time.sleep(0.1) # not sure what to do here, just keep loop running

  def stop_recording(self):
    if (not self.recording): return

    self.recording = False
    self.encoder.output.stop()
    self.picam2.stop_encoder()
    cmd = 'ffmpeg -framerate 30 -i ' + self.video_filename
    cmd += ' -c copy ' + self.video_filename + '.mp4'
    os.system(cmd)
