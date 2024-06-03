# Arduino Storage Cart 

## Overview
The arduino storage cart is a modularly built storage solution for small electronic components or really anything that fits in a tacklebox. Designed to be scalable and customizable, the system uses 3d printed innerlocking joints that fit into wooden dowels to create a skeleton to be filled with "tackle boxes." These boxes correspond to LEDs wired using category 5e UTP (unsheilded twisted pair) cable. In order to interface with the cart, an adafruit featherwing nrf52840 express mounted to a custom PCB (printed circuit board) running circuit python firmware interfaces with via ble with a self hosted sql databased server.

## Tech Stack

### Programming Stack

- **MySQL**: A lightweight SQL compliant database serves as the backbone of the storage cart system, allowing for simple deployment and maintenance by individuals and groups alike.
- **Circuit Python**: A high level programming language used to control low level hardware functions allows firmware code to be readable and thus highly maintainable by virutally any skill level.
- **Flask Web Server**: Extensible python webserver to allow for an easy to access front end across your entire network. (web facing deployment is NOT reccomended).
- **NGINX Reverse Proxy**: Secure reverse proxy server to handle http and https requests inside your network.
- **BLE Nordic Uart**: Serial BLE wrapper to manage communication between the storage cart and server.
- **Python Multiprocessing**: Multiprocessing to allow asynchronous communications to occur independent from web server functions streamlines code. Mutex locks are used to share data between processes.

### Hardware Stack

-**Adafruit nrf52840**: An affordable ble and circuit python capable arduino device.
-**Custom PCB**: A printed circuit board with rj45 connectors to control up to 64 leds with 128 wires using only 16 GPIO pins.
-**3d Printed Chassis**: Easily reproducable plastic components simplify replication and deployment of storage cart systems

## Deployment

Currently planning on deploying with docker-compose. More details to come as project develops further.

## Notice

This project is in the very early stages of planning, this readme will change to reflect the state of the project as it progresses. 