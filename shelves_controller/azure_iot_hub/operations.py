from azure.iot.device.aio import IoTHubDeviceClient
from azure.iot.device import MethodResponse
from .iot_method_name import IoTMethodName
from shelves import control_light, SHELVES
from app.config import config
from app.logger import logger

async def setup_client():
    """
    Sets up the client for Azure IoT Hub communication.

    This function initializes the client and sets the direct method request handler.
    """

    global client
    client = init_client()
    client.on_method_request_received = direct_method_handler
    
def init_client():
    """
    Initializes and returns an instance of the Azure IoT Hub device client.

    Returns:
        IoTHubDeviceClient: An instance of the Azure IoT Hub device client.
    """

    conn_str = f"HostName={config['azureIoTHub']['hostName']};DeviceId={config['deviceId']};SharedAccessKey={config['accessKey']}"
    client = IoTHubDeviceClient.create_from_connection_string(conn_str)

    return client

async def direct_method_handler(method_request):
    """
    Handles the incoming direct method requests from Azure IoT Hub.

    Args:
        method_request (MethodRequest): The method request object containing the details of the method call.
    """
    
    logger.info(f"Received direct method: {method_request.name}")
    logger.info(f"Payload: {method_request.payload}")
    
    if (method_request.name == IoTMethodName.TurnOnLight.name):
        shelf_index = method_request.payload['shelfPosition'] - 1
        if shelf_index < len(SHELVES):
            shelf = SHELVES[shelf_index]
            control_light(shelf, True)
            
    elif (method_request.name == IoTMethodName.TurnOffLight.name):
        shelf_index = method_request.payload['shelfPosition'] - 1
        if shelf_index < len(SHELVES):
            shelf = SHELVES[shelf_index]
            control_light(shelf, False)

    method_response = MethodResponse.create_from_method_request(
        method_request, 200, {}
    )
    await client.send_method_response(method_response)

async def azure_iot_cleanup():
    """
    Cleans up the Azure IoT connection by disconnecting the client.
    """

    await client.disconnect()