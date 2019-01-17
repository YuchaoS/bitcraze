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

            pc.go_to(1,0.4,0.9)
            pc.go_to(1,0,0.9)
            pc.go_to(1,0,1.2)
            pc.go_to(1,0.1,1.2)
            pc.go_to(1,0.1,1.05)

            pc.go_to(1,0.1,1.2)
            pc.go_to(1,0.3,1.2)
            pc.go_to(1,0.3,1.05)
            pc.go_to(1,0.3,1.2)
            pc.go_to(1,0.4,1.2)

            pc.go_to(1,0.4,0.6)
            pc.go_to(1,-0.4,0.6)
            pc.go_to(1,-0.4,1.5)
            pc.go_to(1,-0.3,1.5)
            pc.go_to(1,-0.15,1.7)

            pc.go_to(1,0,1.5)
            pc.go_to(1,0,1.3)
            pc.go_to(1,0,1.5)
            pc.go_to(1,0.4,1.5)
            pc.go_to(1,0.4,1.3)

            pc.go_to(1,0.4,1.5)
            pc.go_to(1,0.55,1.7)
            pc.go_to(1,0.7,1.5)
            pc.go_to(1,0.8,1.5)
            pc.go_to(1,0.8,0.4)

            pc.go_to(1,0.6,0.4)
            pc.go_to(1,0.6,0.6)
            pc.go_to(1,2.6,0.6)
            pc.go_to(1,2.6,1.6)
            pc.go_to(1,2.1,1.6)

            pc.go_to(1,2.1,0.6)
            pc.go_to(1,3.1,0.6)
            pc.go_to(1,3.1,1.6)
            pc.go_to(1,2.9,1.4)
            pc.go_to(1,3.1,1.6)

            pc.go_to(1,3.1,0.6)
            pc.go_to(1,3.9,0.6)
            pc.go_to(1,3.9,0.6)
            pc.go_to(1,3.4,1.6)
            pc.go_to(1,3.4,1.2)

            pc.go_to(1,3.9,1.2)


	
if __name__ == '__main__':
    cflib.crtp.init_drivers(enable_debug_driver=False)
    complex_flight()
