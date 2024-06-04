import time
import asyncio
import websockets

from imu.imu import Imu

imu_left = Imu(0)
imu_right = Imu(1)

imu_left.start()
imu_right.start()

pi_addr = "192.168.1.217"

async def streamMpuData(websocket, path):
  while True:
    il_val = imu_left.accel[2]
    ir_val = imu_right.accel[2]

    # this is super ugly
    dataStr = (
      str(il_val) + "," +
      str(ir_val)
    )

    await websocket.send(
      dataStr
    )

    time.sleep(0.1)

# websocket server
# https://websockets.readthedocs.io/en/stable/intro.html (browser-based example)
# PI_ADDR if internal would be a 192... type address
start_server = websockets.serve(streamMpuData, pi_addr, 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
