import numpy as np


class Check:
    def __init__(self, parameters=None):
        self.parameters = {} if parameters is None else parameters
        self.faults = []

    def safe_positive(self, value):
        """Return a finite, strictly positive scalar as a float."""
        try:
            scalar = np.asarray(value, dtype=float)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError("Value must be a finite positive scalar.") from exc
        if scalar.shape != () or not np.isfinite(scalar) or scalar <= 0.0:
            raise ValueError("Value must be a finite positive scalar.")
        return float(scalar)

    def safe_vector(self, vector):
        """Return a copy of a finite three-component vector as a NumPy array."""
        try:
            values = np.array(vector, dtype=float, copy=True)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError("Vector must contain exactly three finite components.") from exc
        if values.shape != (3,) or not np.all(np.isfinite(values)):
            raise ValueError("Vector must contain exactly three finite components.")
        return values

    def safe_gains(self, kp, ki, kd):
        """Return finite, non-negative PID gains as a tuple of floats."""
        try:
            values = np.asarray([kp, ki, kd], dtype=float)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError("PID gains must be finite non-negative scalars.") from exc
        if (values.shape != (3,) or not np.all(np.isfinite(values))
                or np.any(values < 0.0)):
            raise ValueError("PID gains must be finite non-negative scalars.")
        return tuple(float(value) for value in values)

    def safe_controller_parameters(self, kp, ki, kd, meters_per_count,
                                   bottom_offset, max_pwm, depth_tolerance,
                                   integral_limit):
        """Validate fishing-depth PID parameters, raising ValueError if invalid."""
        try:
            values = np.asarray([kp, ki, kd, meters_per_count, bottom_offset,
                                 max_pwm, depth_tolerance, integral_limit], dtype=float)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError("Controller parameters must be finite scalars.") from exc
        if values.shape != (8,) or not np.all(np.isfinite(values)):
            raise ValueError("Controller parameters must be finite scalars.")
        if np.any(values[:3] < 0.0):
            raise ValueError("PID gains must be non-negative.")
        if meters_per_count <= 0.0 or bottom_offset <= 0.0:
            raise ValueError("Meters per count and bottom offset must be positive.")
        if not 0.0 < max_pwm <= 1.0:
            raise ValueError("Maximum PWM must be in (0, 1].")
        if depth_tolerance < 0.0 or integral_limit < 0.0:
            raise ValueError("Depth tolerance and integral limit must be non-negative.")

    def safe_depth_inputs(self, sounder_depth, hall_counts, dt):
        """Return validated depth, net Hall count, and time step as floats."""
        try:
            values = np.asarray([sounder_depth, hall_counts, dt], dtype=float)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError(
                "Sounder depth, Hall counts, and time step must be finite scalars.") from exc
        if values.shape != (3,) or not np.all(np.isfinite(values)):
            raise ValueError("Sounder depth, Hall counts, and time step must be finite scalars.")
        sounder_depth, hall_counts, dt = values
        if sounder_depth <= 0.0 or dt <= 0.0:
            raise ValueError("Sounder depth and time step must be positive.")
        if hall_counts < 0 or hall_counts != np.floor(hall_counts):
            raise ValueError("Hall counts must be a non-negative net integer count.")
        return float(sounder_depth), float(hall_counts), float(dt)
