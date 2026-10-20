class Sounder:
    """Read network sounder depth in meters below the water surface."""

    def __init__(self, connection=None, transducer_offset_m=0.0, timeout_s=1.0):
        self.connection = connection
        self.transducer_offset_m = transducer_offset_m
        self.timeout_s = timeout_s
        self.depth = None
        self.last_received_time = None

    def read(self):
        """Read a network message and return the latest surface-referenced depth."""
        pass

    def parse_depth(self, message):
        """Extract depth in meters and add the transducer's depth below the surface."""
        pass
