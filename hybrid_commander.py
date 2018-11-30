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
            pc.default_velocity=0.3,
        #print('to mc take off')
        #mc.take_off(1.2,0.3)
        #time.sleep(1)
        #print(pc.get_position())
        #print('to pc take off')
        #pc.take_off(1.70,0.3)
        #print(pc.get_position())
        #print('after take off')
        #time.sleep(1.5)
        #mc.circle_right(0.5, velocity = 0.3,angle_degrees = 360)
        #time.sleep(1.5)
        #mc.land(0.2)
            print(pc.get_position())
            print('pc.go_to(1.5, 0, 1.6)')
            pc.go_to(0, 0, 1.6)
            print(pc.get_position())
            pc.go_to(2, 0, 1.6)
            print(pc.get_position())
            pc.go_to(2, 2, 1.6)
            print(pc.get_position())
            pc.go_to(0, 2, 1.6)
            print(pc.get_position())
            pc.go_to(0, 0, 1.6)
            print(pc.get_position())
        #print('to pc land')
        #pc.land(0.3)
        #print(pc.get_position())
        #print('landed')

