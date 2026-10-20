class HallSensor:
    """Track net cable payout from a spool magnet and Hall-effect sensor.

    A single sensor cannot determine rotation direction; supply it externally.
    Zero counts correspond to fully retrieved cable. Cable payout approximates
    fishing depth only when the cable hangs vertically.
    """

    def __init__(self, pin=None, meters_per_count=None, debounce_s=0.005):
        self.pin = pin
        self.meters_per_count = meters_per_count
        self.debounce_s = debounce_s
        self.counts = 0
        self.position = 0.0
        self.last_pulse_time = None

    def record_pulse(self, direction):
        """Count a debounced pulse: direction 1 pays out and 0 reels in."""
        pass

    def read(self):
        """Return the net Hall count for the depth controller."""
        pass

    def get_depth(self):
        """Return estimated depth in meters using calibrated meters per count."""
        pass

    def reset(self):
        """Zero the count and depth when the cable is fully retrieved."""
        pass
