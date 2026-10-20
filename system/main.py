class BoatSystem:
    def __init__(self, parameters=None, positioning=None, motor=None, protection=None, gear_pid=None, micro_motor_pid=None, hardware=None, display=None):
        self.parameters = {} if parameters is None else parameters
        self.positioning = positioning
        self.motor = motor
        self.protection = protection
        self.gear_pid = gear_pid
        self.micro_motor_pid = micro_motor_pid
        self.hardware = hardware
        self.display = display

    def construct_objects(self):
        pass

    def simulation(self):
        pass
