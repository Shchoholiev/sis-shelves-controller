import asyncio
from shelves import SHELVES, setup_laser_motion_sensor, shelves_cleanup, monitor_laser_motion_sensor
from azure_iot_hub import azure_iot_cleanup, setup_client
from logger import logger

async def main():
    await setup_client()
    setup_laser_motion_sensor()

    motion_sensors_tasks = [monitor_laser_motion_sensor(shelf) for shelf in SHELVES]

    stop_event = asyncio.Event()

    try:
        await asyncio.gather(
            *motion_sensors_tasks,
            stop_event.wait()  # Waiting for stop event
        )
    except:
        logger.info("Application stopping...")
    finally:
        await azure_iot_cleanup()
        shelves_cleanup()
        logger.info("Application stopped.")

def run():
    logger.info("Starting shelves controller...")
    asyncio.run(main())

if __name__ == "__main__":
    run()
