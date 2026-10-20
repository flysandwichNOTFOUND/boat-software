class CalculatePositioning:
    def __init__(self, parameters=None):
        self.parameters = {} if parameters is None else parameters
        self.position = None
        self.depth = None
        self.hall_position = None

    def calculate_position(self, navigation, depth, hall_position):
        pass
