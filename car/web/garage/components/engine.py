from .hardware.pwm import Pwm

class Engine:
    "Engine of the car. It controls the motors' speed."

    def __init__(self, left, right):
        """Initializator."""
        self._pwm = Pwm()
        self._motor_left = left
        self._motor_right = right

    def set_speed(self, speed):
        """Set speed of both motors."""
        self._pwm.set_value(self._motor_left, 0, speed)
        self._pwm.set_value(self._motor_right, 0, speed)
