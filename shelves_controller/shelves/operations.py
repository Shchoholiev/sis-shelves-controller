import asyncio
from .shelf import Shelf
import RPi.GPIO as GPIO
import requests
from .shelves_config import SHELVES
from app.config import config
from app.logger import logger

def setup_shelves():
    """
    Set up the shelves by configuring GPIO and setting up the laser motion sensors and light pins.
    """

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for shelf in SHELVES:
        setup_laser_motion_sensor(shelf)
        GPIO.setup(shelf.light_pin, GPIO.OUT)

def setup_laser_motion_sensor(shelf: Shelf):
    """
    Sets up the laser motion sensor for the given shelf by configuring GPIO.

    Args:
        shelf (Shelf): The shelf object for which the laser motion sensor is being set up.
    """

    GPIO.setup(shelf.laser_beam_pin, GPIO.OUT)
    GPIO.output(shelf.laser_beam_pin, GPIO.HIGH)
    GPIO.setup(shelf.laser_sensor_pin, GPIO.IN)

    logger.info(f"Laser motion sensor set up for shelf {shelf.position}")

def control_light(shelf: Shelf, turn_on: bool):
    """
    Controls the light for a given shelf using GPIO.

    Args:
        shelf (Shelf): The shelf object representing the shelf to control the light for.
        turn_on (bool): If True, turns the light on. If False, turns it off.
    """

    GPIO.output(shelf.light_pin, GPIO.HIGH if turn_on else GPIO.LOW)
    logger.info(f"Light {'on' if turn_on else 'off'} for shelf {shelf.position}")

async def monitor_laser_motion_sensor(shelf: Shelf):
    """
    Monitors the laser motion sensor of a shelf and sends a POST request to the back-end API
    when motion is detected or stopped.

    Args:
        shelf (Shelf): The shelf object representing the shelf to monitor.
    """

    current_state = GPIO.input(shelf.laser_sensor_pin)

    while True:
        if GPIO.input(shelf.laser_sensor_pin) != current_state:
            current_state = GPIO.input(shelf.laser_sensor_pin)
            if current_state == 1:
                logger.info(f"Motion detected on shelf {shelf.position}")

            else:
                logger.info(f"Motion stopped on shelf {shelf.position}")

                url = f"{config['apiUrl']}/shelf-controllers/{config['deviceId']}/shelf/{shelf.position}/movements"
                response = requests.post(url)

                logger.info(f"POST request sent to {url}. Response status code: {response.status_code}")
                
        await asyncio.sleep(0.2)  # Sleep for a short period to prevent blocking

def shelves_cleanup():
    """
    Cleans up the GPIO pins used by the shelves.

    This function should be called when the shelves are no longer in use to release the resources
    used by the GPIO pins.
    """
    
    GPIO.cleanup()
    
    logger.info("GPIO pins cleaned up")
