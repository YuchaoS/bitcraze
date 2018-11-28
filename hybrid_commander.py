import cflib.crtp
import time
import logging

from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.positioning.position_hl_commander import PositionHlCommander

URI = 'radio://0/10/2M/E7E7E7E7E7'


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
      # We take off when the commander is create
        mc = MotionCommander(scf)
        pc = PositionHlCommander(scf)
        mc.take_off(1.2,0.3)
        time.sleep(1)
        pc.take_off(1.8,0.3)
        #time.sleep(1.5)
        #mc.circle_right(0.5, velocity = 0.3,angle_degrees = 360)
        #time.sleep(1.5)
        #mc.land(0.2)
        pc.go_to(2.0, 2.0, 1.0)
        time.sleep(3)
        print('to land')
        pc.land(0.3)
        print('landed')
   

