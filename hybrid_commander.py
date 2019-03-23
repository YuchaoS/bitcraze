import cflib.crtp
import time
import logging

from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger

from cflib.crazyflie import Crazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.positioning.position_hl_commander import PositionHlCommander

URI = 'radio://0/50/2M/E7E7E7E7E7'

def position_callback(timestamp, data, logconf):
    print(data)

if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
      # We take off when the commander is create
        with PositionHlCommander(scf) as pc:
            print('after take off, to sleep 1s')
            log_conf = LogConfig(name='Position', period_in_ms=500)
            log_conf.add_variable('kalman.stateX', 'float')
            log_conf.add_variable('kalman.stateY', 'float')
            log_conf.add_variable('kalman.stateZ', 'float')
            scf.cf.log.add_config(log_conf)
            log_conf.data_received_cb.add_callback(position_callback)
            log_conf.start()
            cf = scf.cf
            time.sleep(1)
            x=0.5
            y=0.5
            z=1.0
            pc.default_velocity=0.3
            pc.go_to(-x,-y,0.3)
            time.sleep(2)
            print('1')
            pc.go_to(-x,-y,z)
            time.sleep(1)
            print('2')
            pc.go_to(x,-y,z)
            time.sleep(1)
            #cf.commander.send_hover_setpoint(0, 0, 90, z)
            #time.sleep(1)
            print('3')
            pc.go_to(x,y,z)
            time.sleep(1)
            #cf.commander.send_hover_setpoint(0, 0, 90, z)
            #time.sleep(1)
            print('4')
            pc.go_to(-x,y,z)
            time.sleep(1)
            #cf.commander.send_hover_setpoint(0, 0, 90, z)
            #time.sleep(1)
            print('5')
            pc.go_to(-x,-y,z)
            time.sleep(1)
            #cf.commander.send_hover_setpoint(0, 0, 90, z)
            #time.sleep(1)
            print('6')
            pc.go_to(-1.0,-1.0,0.3)
            time.sleep(1)
            time.sleep(1)
           ## pc.go_to(2.0,1.5,0.2)
           ## time.sleep(2)
            '''
            pc.default_velocity=0.3,
            print(pc.get_position())
            pc.go_to(0, 0, 1.0)
            print(pc.get_position())
            time.sleep(1)
            pc.go_to(1.5, 0, 1.0)
            print(pc.get_position())
            time.sleep(1)
            pc.go_to(1.5, 1.5, 1.0)
            print(pc.get_position())
            time.sleep(1)
            pc.go_to(0, 1.5, 1.0)
            print(pc.get_position())
            time.sleep(1)
            pc.go_to(0, 0, 1.0)
            '''
