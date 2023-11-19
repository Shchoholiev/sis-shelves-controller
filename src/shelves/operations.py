import asyncio
import RPi.GPIO as GPIO
import requests
from shelves_config import SHELVES

def setup_shelves():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for shelf in SHELVES:
        setup_laser_motion_sensor(shelf)
        GPIO.setup(shelf.light_pin, GPIO.OUT)

def setup_laser_motion_sensor(shelf):
    GPIO.setup(shelf.laser_beam_pin, GPIO.OUT)
    GPIO.output(shelf.laser_beam_pin, GPIO.HIGH)
    GPIO.setup(shelf.laser_sensor_pin, GPIO.IN)

def turn_on_light(shelf):
    GPIO.output(shelf.light_pin, GPIO.HIGH)

def turn_off_light(shelf):
    GPIO.output(shelf.light_pin, GPIO.LOW)

async def monitor_laser_motion_sensor(shelf):
    current_state = GPIO.input(shelf.laser_sensor_pin)

    while True:
        if GPIO.input(shelf.laser_sensor_pin) != current_state:
            current_state = GPIO.input(shelf.laser_sensor_pin)
            if current_state == 1:
                print("Motion detected!")
            else:
                print("Motion stopped!")
                url = f"https://smart-inventory-system.azurewebsites.net/shelf-controllers/7948ae2e-4161-4fbc-9380-3eb7fa0751c5/shelf/{shelf.position}/movements"  # Replace with the actual URL
                response = requests.post(url)
                print(response.status_code)
                
        await asyncio.sleep(0.2)  # Sleep for a short period to prevent blocking

def shelves_cleanup():
    GPIO.cleanup()