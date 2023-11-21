from .shelf import Shelf

SHELVES = [
    Shelf(
        laser_sensor_pin=8, 
        laser_beam_pin=21, 
        light_pin=7,
        position=1
    ),
    Shelf(
        laser_sensor_pin=14, 
        laser_beam_pin=20, 
        light_pin=25,
        position=2
    ),
    Shelf(
        laser_sensor_pin=15, 
        laser_beam_pin=16, 
        light_pin=18,
        position=3
    ),
    Shelf(
        laser_sensor_pin=23, 
        laser_beam_pin=12, 
        light_pin=24,
        position=4
    ),
]