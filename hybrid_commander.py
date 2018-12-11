import cflib.crtp
import time
import logging

from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.positioning.position_hl_commander import PositionHlCommander

URI = 'radio://0/0/2M/E7E7E7E7E7'


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
      # We take off when the commander is create
        with PositionHlCommander(scf) as pc:
            print('after take off, to sleep 1s')
            time.sleep(1)
            pc.default_velocity=0.3,
            print(pc.get_position())
            pc.go_to(0, 0, 1.6)
            print(pc.get_position())
            time.sleep(1)
            pc.go_to(2.5, 0, 1.6)
            print(pc.get_position())
            time.sleep(1)
            pc.go_to(2.5, 2.5, 1.6)
            print(pc.get_position())
            time.sleep(1)
            pc.go_to(0, 2.5, 1.6)
            print(pc.get_position())
            time.sleep(1)
            pc.go_to(0, 0, 1.6)
