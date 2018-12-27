import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/60/2M/E7E7E7E7E7'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        # We take off when the commander is create
        mc = MotionCommander(scf)
        mc.take_off(0.5,0.3)
        time.sleep(1)
        mc.circle_right(1, velocity = 0.6,angle_degrees = 180)
        mc.up(0.5)
        mc.circle_right(1, velocity = 0.6,angle_degrees = 180)
        mc.land(0.2)
        
