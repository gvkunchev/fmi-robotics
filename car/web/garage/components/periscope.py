from .hardware.servo import Servo


class Periscope:
    "Periscope on which the camera is mounted and can pan/tilt."

    POSITIONS = 5

    def __init__(self, pan_port, tilt_port, pan_min, pan_max, tilt_min, tilt_max):
        """Initializator."""
        self._pan_min = pan_min
        self._tilt_min = tilt_min
        self._pan_step = (pan_max - pan_min) // self.POSITIONS
        self._tilt_step = (tilt_max - tilt_min) // self.POSITIONS
        self._pan_servo = Servo(pan_port, pan_min, pan_max)
        self._tilt_servo = Servo(tilt_port, tilt_min, tilt_max)

    def pan(self, position):
        """Pan to a set position."""
        self._pan_servo.set(self._pan_min + position*self._pan_step)

    def tilt(self, position):
        """Tilt to a set position."""
        self._tilt_servo.set(self._tilt_min + position*self._tilt_step)
