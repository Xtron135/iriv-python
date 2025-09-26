import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Set GPIO 17 as output
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

# Turn on the LED
GPIO.output(LED_PIN, GPIO.HIGH)

print("LED is ON")

# Keep it on for 5 seconds
time.sleep(5)

# Turn off the LED
GPIO.output(LED_PIN, GPIO.LOW)
print("LED is OFF")

# Clean up GPIO settings
GPIO.cleanup()
