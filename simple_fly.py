import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.position_hl_commander import PositionHlCommander

# URI to the Crazyflie to connect to
uri = 'radio://0/80/2M/E7E7E7E7E7'


def complex_flight():
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:
        with PositionHlCommander(
                scf,
                x=1.0, y=1.0, z=0.0,
                default_velocity=0.3,
                default_height=0.5,
                controller=PositionHlCommander.CONTROLLER_MELLINGER) as pc:
            pc.set_default_velocity(0.3)
            pc.set_default_height(1.0)
            #pc.go_to(1.0, 1.0)
            pc.go_to(3.0, 1.0)
            pc.go_to(2.0, 3.0)
            pc.go_to(1.0, 1.0)

if __name__ == '__main__':
    cflib.crtp.init_drivers(enable_debug_driver=False)
    complex_flight()
