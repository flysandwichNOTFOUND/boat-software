class NMEA0183Reader:
    def __init__(self, port=None, baudrate=4800):
        self.port = port
        self.baudrate = baudrate
        self.connection = None
        self.speed_over_ground = None
        self.course_over_ground = None

    def read(self):
        pass

    def parse(self, sentence):
        pass
