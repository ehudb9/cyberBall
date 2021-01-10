import socket
import _thread
from venv.Experiment.constants import *
from venv.Experiment.arm_movement_control import ArmMotorControl


class TcpControlMode:
    def __init__(self):
        self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serversock.bind(ADDRESS)
        self.serversock.listen(5)
        self.arm = ArmMotorControl()

    def start(self):
        print('waiting for connection... listening on port', PORT)

        while 1:
            clientsock, address = self.serversock.accept()
            # print('...connected from:', address)
            _thread.start_new_thread(self.handler, (clientsock, address))

    @staticmethod
    def response(key):
        return 'Server response: ' + key

    def handler(self, clientsock, address):
        while 1:
            data_as_byte = clientsock.recv(BUFF)
            if not data_as_byte:
                break

            data_as_string = data_as_byte.decode("utf-8")
            data_as_string = str(data_as_string)

            if data_as_string == "ArmClockWise":
                self.arm.turn_clockwise(MOTOR_NAME)
                print("Clockwise sent")
            elif data_as_string == "ArmCounterClockWise":
                self.arm.turn_counter_clockwise(MOTOR_NAME)
                print("Counter clockwise sent")
            else:
                print(f"Received but not understood: {data_as_string}")
            if "close" == data_as_byte.rstrip():
                print("Closing ...")
                break  # type 'close' on client console to close connection from the server side

        clientsock.close()
        print(address, "- closed connection")  # log on console
