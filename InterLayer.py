import threading

# Mode selection
UNINIT = 0
UART = 1
I2C = 2

import serial


class InterLayer(threading.Thread):
    mode = UNINIT

    # if using serial
    serialPort = None
    baudrate = 115200
    #####
    # Public Interface
    #####

    def __init__(self, mode=UART, baudrate=9600):
        self.mode = mode
        #
        # if using uart
        self.init_serial()
        self.baudrate = baudrate
        #
        # if using I2C

    def init_serial(self):
        self.serialPort = serial.Serial(
            port='/dev/ttyAMA1',
            baudrate= self.baudrate,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0
        )


    def receive(self):
        # return "sample message"
        return self.serialPort.read(65536).decode("utf-8") 

    def send(self, data):
        print("Sent: ", data)
        # return 1
        return self.serialPort.write(str.encode(data))