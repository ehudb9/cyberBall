from venv.Experiment.control_modes.keyboard_control_mode import KeyboardControlMode
from venv.Experiment.control_modes.tcp_control_mode import TcpControlMode
from venv.Experiment.arm_movement_control import ArmMotorControl
from venv.Experiment.constants import *
import time

if __name__ == '__main__':
    keyboard_mode = KeyboardControlMode()
    #tcp_mode = TcpControlMode()

    #keyboard_mode.start()
    #tcp_mode.start()
    '''
    arm = ArmMotorControl()
    arm.set_moving_speed(MOTOR_NAME, 120)
    arm.set_acceleration(MOTOR_NAME, 2)

    for i in range(12):
        arm.turn_counter_clockwise(MOTOR_NAME)
        time.sleep(3)

'''