import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander

URI = 'radio://0/70/2M'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        # We take off when the commander is create
        mc = MotionCommander(scf)
        time.sleep(1)
        mc.take_off(1.2,0.3)
        time.sleep(1.5)
        mc.circle_right(0.5, velocity = 0.3,angle_degrees = 360)
        time.sleep(1.5)
        mc.land(0.2)
        
