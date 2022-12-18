from .hardware.servo import Servo


class Wheel:
    "Wheel that can make the care turn left/right"

    def __init__(self, port, min, max):
        """Initializator."""
        self._min = min
        self._max = max
        self._servo = Servo(port, min, max)

    def left(self):
        """Turn left."""
        self._servo.set(self._min)

    def right(self):
        """Turn right."""
        self._servo.set(self._max)

    def center(self):
        """Turn center."""
        self._servo.set(self._min + (self._max - self._min) // 2)
