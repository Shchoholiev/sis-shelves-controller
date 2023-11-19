import asyncio
from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import MethodResponse
from src.enums.iot_method_name import IoTMethodName
from src.configs.shelves_config import SHELVES
import RPi.GPIO as GPIO

async def init_client():
    conn_str = "HostName=smart-inventory-system.azure-devices.net;DeviceId=7948ae2e-4161-4fbc-9380-3eb7fa0751c5;SharedAccessKey=/vQPktdneAdDhyBU0oShvlhhfpyOSLOMWAIoTLYX35Y="
    client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    return client

async def direct_method_handler(method_request):
    print(f"Received direct method: {method_request.name}")
    print(f"Payload: {method_request.payload}")

    
    if (method_request.name == IoTMethodName.TurnOnLight.name):
        shelf_index = method_request.payload['shelfPosition'] - 1
        if shelf_index < len(SHELVES):
            print("Turning on light")

            shelf = SHELVES[shelf_index]
            GPIO.setup(shelf.light_pin, GPIO.OUT)
            GPIO.output(shelf.light_pin, GPIO.HIGH)
            
    elif (method_request.name == IoTMethodName.TurnOffLight.name):
        shelf_index = method_request.payload['shelfPosition'] - 1
        if shelf_index < len(SHELVES):
            print("Turning off light")

            shelf = SHELVES[shelf_index]
            GPIO.setup(shelf.light_pin, GPIO.OUT)
            GPIO.output(shelf.light_pin, GPIO.LOW)
    

    # Respond to the direct method call
    print("Responding")
    method_response = MethodResponse.create_from_method_request(
        method_request, 200, {}
    )
    await client.send_method_response(method_response)


async def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    global client 
    client = await init_client()
    client.on_method_request_received = direct_method_handler

    stop_event = asyncio.Event()

    try:
        await stop_event.wait()  # This will wait indefinitely until stop_event is set
    except:
        print("Application stopping...")
    finally:
        await client.disconnect()
        GPIO.cleanup()
        print("Application stopped")

if __name__ == "__main__":
    print("Starting shelves controller")
    asyncio.run(main())
