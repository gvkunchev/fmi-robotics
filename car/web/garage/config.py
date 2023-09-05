# Pins on the PWM controller connected to the
# motor driver for controlling the speed
LEFT_MOTOR_SPEED = 5
RIGHT_MOTOR_SPEED = 4

# Definition of speed values as used by the PWM controller
# The controller supports 0-4095, but limits are either
# too low to produce any movement or too dangerous for the car
MIN_SPEED = 500
MAX_SPEED = 4000

# Pins on the PI board connected to the
# motor driver for controlling the direction
LEFT_MOTOR_FWD = 17
LEFT_MOTOR_BWD = 18
RIGHT_MOTOR_FWD = 22
RIGHT_MOTOR_BWD = 27

# Wheel port and min/max angles for turning the servo
WHEEL_PORT = 0
WHEEL_MIN = 67
WHEEL_MAX = 120

# Distance sensor pins on the Pi
DIST_SENSOR_TRIG = 14
DIST_SENSOR_ECHO = 15

# Periscope tilt port and min/max angles
TILT_PORT = 1
TILT_MIN = 20
TILT_MAX = 180

# Periscope pan port and min/max angles
PAN_PORT = 2
PAN_MIN = 20
PAN_MAX = 180
