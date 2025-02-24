import RPi.GPIO as GPIO
import time

# Define the GPIO pin where the servo is connected
SERVO_PIN = 18
SERVO_PIN2 = 13

# Set up the GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(SERVO_PIN2, GPIO.OUT)

# Initialize PWM on the servo pin at 50Hz
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(2.5)  # Start at 0° position (duty cycle may vary based on your servo)
pwm2 = GPIO.PWM(SERVO_PIN2, 50)
pwm2.start(2.5)

try:
    # Move to 0° (approximately 2.5% duty cycle)
    pwm.ChangeDutyCycle(2.5)
    pwm2.ChangeDutyCycle(2.5)
    time.sleep(1)

    # Move to 90° (approximately 7.5% duty cycle)
    pwm.ChangeDutyCycle(7.5)
    pwm2.ChangeDutyCycle(7.5)
    time.sleep(1)

    # Move to 180° (approximately 12.5% duty cycle)
    pwm.ChangeDutyCycle(12.5)
    pwm2.ChangeDutyCycle(12.5)
    time.sleep(1)

    # Optionally, return to 0°
    pwm.ChangeDutyCycle(2.5)
    pwm2.ChangeDutyCycle(2.5)
    time.sleep(1)

finally:
    # Stop PWM and clean up GPIO settings
    pwm.stop()
    pwm2.stop()
    GPIO.cleanup()

