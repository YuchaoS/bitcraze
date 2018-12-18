import cflib.crtp
import time
import logging
import math

from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.positioning.position_hl_commander import PositionHlCommander

URI = 'radio://0/10/2M/E7E7E7E7E7'

def circle_left(self,radius_m,velocity):
    time.sleep(1)
    x_ini=self._x
    y_ini=self._y
    z_ini=self._z
    #time=angle_degree*radius_m*math.pi/velocity/360
    for i in range(1,40):
        go_to(x_ini+radius*math.cos(2*math.pi/40*i),
        y_ini+radius*math.sin(2*math.pi/40*i),
        z_ini,velocity)
        time.sleep(0.2)
		
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
            circle_left(1,0.3)

