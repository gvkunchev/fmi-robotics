from adafruit_servokit import ServoKit


class Servo:
    "Servo that can rotate from about 0 to 180 degrees"

    def __init__(self, port, min, max):
        """Initializator."""
        self._port = port
        self._iface = ServoKit(channels=8).servo[port]
        self._min = min
        self._max = max

    def set(self, value):
        """Set rotation based on an angle value."""
        value = max(value, self._min)
        value = min(value, self._max)
        self._iface.angle = value
