from . import config
from .components.engine import Engine
from .components.transmission import Transmission
from .components.wheel import Wheel
from .components.hardware.distance_sensor import DistanceSensor


class Car:
    "Car object that controls all pieces on board."

    def __init__(self):
        """Initializator."""
        self._engine = Engine(left=config.LEFT_MOTOR_SPEED,
                              right=config.RIGHT_MOTOR_SPEED)
        self._transmission = Transmission(left_fwd=config.LEFT_MOTOR_FWD,
                                          left_bwd=config.LEFT_MOTOR_BWD,
                                          right_fwd=config.RIGHT_MOTOR_FWD,
                                          right_bwd=config.RIGHT_MOTOR_BWD)
        self._wheel = Wheel(port=config.WHEEL_PORT,
                            min=config.WHEEL_MIN,
                            max=config.WHEEL_MAX)
        self._distance_sensor = DistanceSensor(trig=config.DIST_SENSOR_TRIG,
                                               echo=config.DIST_SENSOR_ECHO)

    def fwd(self):
        """Move forward."""
        self._transmission.fwd()

    def bwd(self):
        """Move backward."""
        self._transmission.bwd()

    def stop(self):
        """Stop moving."""
        self._transmission.stop()

    def set_speed(self, gear):
        """Set moving speed by ratio between 0 and 1."""
        speed = int((config.MAX_SPEED - config.MIN_SPEED) * float(gear))
        self._engine.set_speed(speed)

    def left(self):
        """Turn left."""
        self._wheel.left()

    def right(self):
        """Turn right."""
        self._wheel.right()

    def center(self):
        """Turn center."""
        self._wheel.center()
    
    def get_distance(self):
        """Get distance from the sensor."""
        return self._distance_sensor.read()
