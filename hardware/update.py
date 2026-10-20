class HardwareUpdate:
    def __init__(self, nmea_reader=None, sounder=None, hall_sensor=None, motor_interface=None):
        self.nmea_reader = nmea_reader
        self.sounder = sounder
        self.hall_sensor = hall_sensor
        self.motor_interface = motor_interface

    def update(self):
        pass
