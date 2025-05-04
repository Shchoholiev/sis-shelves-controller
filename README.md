# sis-shelves-controller
A Python-based controller for managing shelves with laser motion sensors and lights, integrated with Azure IoT Hub for remote operations.

## Table of Contents
- [Features](#features)
- [Stack](#stack)
- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup Instructions](#setup-instructions)
- [Configuration](#configuration)

## Features
- Real-time monitoring of laser motion sensors on shelves.
- Control of shelf lights via GPIO pins on Raspberry Pi.
- Azure IoT Hub integration for remote control and direct method handling.
- Logging with rotating file handler for operational insights.
- Configurable through JSON files for easy deployment changes.

## Stack
- Python 3.9+
- Azure IoT Device SDK (`azure-iot-device==2.12.0`)
- Raspberry Pi GPIO (`RPi.GPIO`)
- Asyncio for asynchronous sensor monitoring and Azure IoT communication
- Requests for backend API integration
- Logging with Python standard library

## Installation

### Prerequisites
- Raspberry Pi with GPIO pins (or compatible device)
- Python 3.9 or higher installed
- Internet connection for installing dependencies and Azure IoT Hub access
- Access to Azure IoT Hub with device connection string credentials

### Setup Instructions

1. Clone the repository or download the source code:
   ```bash
   git clone https://github.com/Shchoholiev/sis-shelves-controller.git
   cd sis-shelves-controller
   ```

2. Create and activate a Python virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Install the package locally:
   ```bash
   python setup.py install
   ```

5. Configure the application by editing the `shelves_controller/app/appconfig.json` and creating/modifying `deviceconfig.json` with your device-specific settings (see Configuration section).

6. Run the controller:
   ```bash
   shelvescontroller
   ```
   Or run directly via Python:
   ```bash
   python -m shelves_controller.app.app
   ```

## Configuration
The application relies on two JSON configuration files located in `shelves_controller/app/`:

- `appconfig.json`: Contains general configuration such as backend API URLs and Azure IoT Hub host name.
  
  Example snippet:
  ```json
  {
      "apiUrl": "https://smart-inventory-system.azurewebsites.net",
      "azureIoTHub": {
          "hostName": "smart-inventory-system.azure-devices.net"
      }
  }
  ```

- `deviceconfig.json` (must be created): Contains device-specific credentials for Azure IoT Hub connectivity.

  Required fields:
  ```json
  {
      "deviceId": "your-device-id",
      "accessKey": "your-device-access-key"
  }
  ```

Ensure both files are present for the system to connect to Azure IoT Hub and the backend API properly.
