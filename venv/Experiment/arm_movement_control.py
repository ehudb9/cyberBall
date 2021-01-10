from .butter_connector import ButterConnector
from .constants import *
import sys


class ArmMotorControl:

    def __init__(self):
        self.butterHttpClient = ButterConnector(ROBOT_IP).butterHttpClient

    def reset_offset(self, motor_name):
        self.butterHttpClient.setMotorRegister(motor_name, 'multi-turn-offset', '0')

    def parse_response(self, response):
        try:
            response = response['Result']
            response = response.split('|')[1].strip()
            return response
        except:
            e = sys.exc_info()[0]
            print("<p>Error: %s</p>" % e)

    def get_present_position(self, motor_name):
        result = self.butterHttpClient.getMotorRegister(motor_name, 'present-position').json()
        print(result)
        # position_str = self.parse_response(result)

        while result['Executed'] == False:
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            result = self.butterHttpClient.getMotorRegister(motor_name, 'present-position').json()

        position_str = self.parse_response(result)
        return int(position_str)

    def turn_setup(self, motor_name):
        self.reset_offset(motor_name)
        pres_pos = self.get_present_position(motor_name)
        return pres_pos

    def turn_clockwise(self, motor_name):
        pres_pos = self.turn_setup(motor_name)
        goal_pos = int(pres_pos) + THIRD_CIRCLE
        response = self.butterHttpClient.setMotorRegister(motor_name, 'goal-position', str(goal_pos))
        print(response.json())

    def turn_counter_clockwise(self, motor_name):
        pres_pos = self.turn_setup(motor_name)
        goal_pos = int(pres_pos) - THIRD_CIRCLE
        response = self.butterHttpClient.setMotorRegister(motor_name, 'goal-position', str(goal_pos))
        print(response.json())

    def turn_full_circle(self, motor_name):
        pres_pos = self.turn_setup(motor_name)
        goal_pos = int(pres_pos) - FULL_CIRCLE
        response = self.butterHttpClient.setMotorRegister(motor_name, 'goal-position', str(goal_pos))
        print(response.json())

    def set_acceleration(self, motor_name, value):
        response = self.butterHttpClient.setMotorRegister(motor_name, 'goal-acceleration', str(value))
        print(response.json())

    def set_moving_speed(self, motor_name, value):
        response = self.butterHttpClient.setMotorRegister(motor_name, 'moving-speed', str(value))
        print(response.json())