class ESP32Interface:
    def __init__(self, port=None, baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.connection = None

    def connect(self):
        pass

    def read(self):
        pass

    def write(self, data):
        pass

    def disconnect(self):
        pass
