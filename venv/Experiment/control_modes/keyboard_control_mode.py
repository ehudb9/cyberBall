from venv.Experiment.arm_movement_control import ArmMotorControl
from venv.Experiment.constants import *
from pynput import keyboard


class KeyboardControlMode:
    def __init__(self):
        self.arm = ArmMotorControl()
        self.arm.set_moving_speed(MOTOR_NAME, 120)
        self.arm.set_acceleration(MOTOR_NAME, 2)

    def start(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()
            print("Listening started...")

    def on_press(self, key):
        try:
            pass
        except AttributeError:
            print('special key {0} pressed'.format(key))

    def on_release(self, key):
        if key == keyboard.Key.right:
            self.arm.turn_counter_clockwise(MOTOR_NAME)
        if key == keyboard.Key.left:
            self.arm.turn_clockwise(MOTOR_NAME)
        if key == keyboard.Key.up:
            self.arm.turn_full_circle(MOTOR_NAME)
        if key == keyboard.Key.esc:
            # Stop listener
            print("Listening stopped")
            return False
