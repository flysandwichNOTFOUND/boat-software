import numpy as np

from .protection import Check


class GearPID:
    """Control depth below the surface, assuming the cable hangs vertically.

    Hall counts are signed net counts from a zero at fully retrieved cable.
    Sounder depth must use the same surface reference as the fishing depth.
    PWM is normalized to 0..1; direction 1 pays out and 0 reels in.
    """

    def __init__(self, kp, ki, kd, meters_per_count, bottom_offset,
                 max_pwm=1.0, depth_tolerance=0.20, integral_limit=5.0):
        self.protection = Check()
        self.protection.safe_controller_parameters(
            kp, ki, kd, meters_per_count, bottom_offset,
            max_pwm, depth_tolerance, integral_limit)

        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.meters_per_count = meters_per_count
        self.bottom_offset = bottom_offset
        self.max_pwm = max_pwm
        self.depth_tolerance = depth_tolerance
        self.integral_limit = integral_limit
        self.integral = 0.0
        self.previous_depth = None

    def update(self, sounder_depth, hall_counts, dt):
        """Return (PWM duty cycle, direction bit) for the current depth sample."""
        sounder_depth, hall_counts, dt = self.protection.safe_depth_inputs(
            sounder_depth, hall_counts, dt)

        target_depth = max(0.0, sounder_depth - self.bottom_offset)
        fishing_depth = hall_counts * self.meters_per_count
        error = target_depth - fishing_depth

        # Derivative on measured depth avoids a kick when the bottom depth changes.
        depth_rate = (0.0 if self.previous_depth is None else
                      (fishing_depth - self.previous_depth) / dt)
        self.previous_depth = fishing_depth

        if abs(error) <= self.depth_tolerance:
            self.integral = 0.0
            return 0.0, 0

        candidate_integral = float(np.clip(
            self.integral + error * dt, -self.integral_limit, self.integral_limit))
        candidate_output = (self.kp * error + self.ki * candidate_integral
                            - self.kd * depth_rate)
        # Freeze integration when it would push an already saturated output further.
        if abs(candidate_output) <= self.max_pwm or error * candidate_output < 0.0:
            self.integral = candidate_integral

        output = self.kp * error + self.ki * self.integral - self.kd * depth_rate
        # Never pay out when the bait is already deeper than its clearance target.
        if error < 0.0:
            output = min(output, 0.0)
        if hall_counts == 0 and output < 0.0:
            output = 0.0

        pwm = float(np.clip(abs(output), 0.0, self.max_pwm))
        direction = int(output > 0.0)
        return pwm, direction

    def reset(self):
        self.integral = 0.0
        self.previous_depth = None


class MicroMotorPID:
    def __init__(self, kp=0.0, ki=0.0, kd=0.0, setpoint=0.0):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.setpoint = setpoint
        self.integral = 0.0
        self.previous_error = None

    def update(self, motor_score, dt):
        pass

    def reset(self):
        pass
