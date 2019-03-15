import time
import cflib.crtp

from cflib.crazyflie import Crazyflie
from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.crazyflie.syncLogger import SyncLogger

URI = 'radio://0/40/2M/E7E7E7E7E7'

def position_callback(timestamp, data, logconf):
    print(data)

if __name__ == '__main__':
    # Initialize the low-level drivers (don't list the debug drivers)
    cflib.crtp.init_drivers(enable_debug_driver=False)
    log_conf = LogConfig(name='Position', period_in_ms=500)
    log_conf.add_variable('ranging.distance2', 'float')
    #log_conf.add_variable('kalman.stateX', 'float')
    #log_conf.add_variable('kalman.stateZ', 'float')
    #log_conf.add_variable('stabilizer.roll', 'float')
    #log_conf.add_variable('stabilizer.pitch', 'float')
    #log_conf.add_variable('stabilizer.yaw', 'float')

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
        scf.cf.log.add_config(log_conf)
        log_conf.data_received_cb.add_callback(position_callback)
        log_conf.start()
        for i in range(60):
            time.sleep(1)

