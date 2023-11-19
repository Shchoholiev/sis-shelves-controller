from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import MethodResponse
from iot_method_name import IoTMethodName
from shelves import turn_on_light, turn_off_light
from shelves import SHELVES

async def setup_client():
    """Set up the Azure IoT Hub client to handle direct method calls"""

    global client
    client = init_client()
    client.on_method_request_received = direct_method_handler
    
def init_client():
    """Initialize the Azure IoT Hub client"""

    conn_str = "HostName=smart-inventory-system.azure-devices.net;DeviceId=7948ae2e-4161-4fbc-9380-3eb7fa0751c5;SharedAccessKey=/vQPktdneAdDhyBU0oShvlhhfpyOSLOMWAIoTLYX35Y="
    client = IoTHubDeviceClient.create_from_connection_string(conn_str)
    return client

async def direct_method_handler(method_request):
    """Handle direct method calls from Back-End Service"""
    
    print(f"Received direct method: {method_request.name}")
    print(f"Payload: {method_request.payload}")
    
    if (method_request.name == IoTMethodName.TurnOnLight.name):
        shelf_index = method_request.payload['shelfPosition'] - 1
        if shelf_index < len(SHELVES):
            print("Turning on light")

            shelf = SHELVES[shelf_index]
            turn_off_light(shelf)
            
    elif (method_request.name == IoTMethodName.TurnOffLight.name):
        shelf_index = method_request.payload['shelfPosition'] - 1
        if shelf_index < len(SHELVES):
            print("Turning off light")

            shelf = SHELVES[shelf_index]
            turn_on_light(shelf)

    method_response = MethodResponse.create_from_method_request(
        method_request, 200, {}
    )
    await client.send_method_response(method_response)

async def azure_iot_cleanup():
    """Disconnect from Azure IoT Hub"""

    await client.disconnect()