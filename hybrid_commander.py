import cflib.crtp
import time
import logging

from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.positioning.position_hl_commander import PositionHlCommander

URI = 'radio://0/20/2M/E7E7E7E7E7'


if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
      # We take off when the commander is create
        mc = MotionCommander(scf)
        pc = PositionHlCommander(scf)
        #print('to mc take off')
        #mc.take_off(1.2,0.3)
        #time.sleep(1)
        print('to pc take off')
        pc.take_off(1.75,0.3)
        print('after take off')
        #time.sleep(1.5)
        #mc.circle_right(0.5, velocity = 0.3,angle_degrees = 360)
        #time.sleep(1.5)
        #mc.land(0.2)
        print('pc.go_to(1.5, 0, 1.75)')
        pc.go_to(1.5, 0, 1.75)
        print('pc.go_to(1.5, 0, 1.75)')
        pc.go_to(1.5, 1.5, 1.75)
        print('pc.go_to(0, 1.5, 1.75)')
        pc.go_to(0, 1.5, 1.75)
        print('pc.go_to(0, 0, 1.75)')
        pc.go_to(0, 0, 1.75)
        time.sleep(1)
        print('to pc land')
        pc.land(0.3)
        print('landed')

