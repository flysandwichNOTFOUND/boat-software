class DisplayPlot:
    def __init__(self, gear_position=None, speed_over_ground=None, course_over_ground=None):
        self.gear_position = gear_position
        self.speed_over_ground = speed_over_ground
        self.course_over_ground = course_over_ground

    def update(self, gear_position, speed_over_ground, course_over_ground):
        pass

    def plot(self):
        pass
