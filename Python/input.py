import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Set GPIO 18 as input with pull-down resistor
BUTTON_PIN = 18
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Waiting for button press...")

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.HIGH:
            print("Button was pressed!")
            time.sleep(0.2)  # Debounce delay
        else:
            time.sleep(0.05)  # Polling delay
except KeyboardInterrupt:
    print("Exiting program")

GPIO.cleanup()
