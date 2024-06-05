# A Simple Serial Wrapper for consistent syntax in CircuitPython communications
# By Michael Lance
# 5/31/2024
# Updated 5/31/2024
#------------------------------------------------------------------------#
import sys
import time

if sys.implementation.name != 'circuitpython':
    import serial
    import serial.tools.list_ports
elif sys.implementation.name == 'circuitpython':
    import usb_cdc

#------------------------------------------------------------------------#

class SerHandler:
    def __init__(self, baudrate): 
        self.baudrate = baudrate
        self.ser = None
        
        if 'serial' in globals():
            self.mode = "py"
            self._initialize_pyserial()
        else:
            self.mode = "cirpy"
            self._initialize_cirpy()

        if self.mode == "py":
            self.write = self.pywrite
            self.read = self.pyread
            self.if_data = self.pyif_data
        elif self.mode == "cirpy":
            self.write = self.cirpywrite
            self.read = self.cirpyread
            self.if_data = self.cirpyif_data

    def _initialize_pyserial(self):
        print("initializing on pyserial")
        self.connected = False
        while not self.connected:
            ports = list(serial.tools.list_ports.comports())
            for port_info in ports:
                port = port_info.device
                print(f'Attempting: {port}')
                try:
                    ser = serial.Serial(port, self.baudrate, timeout=1)
                    ser.reset_output_buffer()
                    ser.reset_input_buffer()

                    ser.write(b"correct port")
                    time.sleep(1)
                    resp = ser.read(12)
                    print(resp)
                    if resp == b"correct port":
                        print(f'Successfully connected to {port} at {self.baudrate}')
                        self.ser = ser
                        self.connected = True
                        break
                    else:
                        ser.close()
                except Exception as e:
                    print(f'Received error on port {port}: {e}')    

    def _initialize_cirpy(self, debug=False):
        usb_cdc.data.reset_input_buffer()
        usb_cdc.data.reset_output_buffer()

        connected = False
        print("Initializing SerWrap on circuit python")
        print("Launch a compatible python program running serWrap to connect automatically!")
        while not connected:
            if usb_cdc.data.in_waiting > 0:
                message = usb_cdc.data.read(12)
                if debug == True:
                    print(f"message recieved: {message}")

                if message == b"correct port":
                    usb_cdc.data.write(b"correct port")
                    connected = True
                    print("Found port, connecting")
                    time.sleep(1)
    
    def pywrite(self, data):
        return self.ser.write(data)
        
    def cirpywrite(self, data):
        return usb_cdc.data.write(data)
    
    def pyread(self, size):
        return self.ser.read(size)
    
    def cirpyread(self, size):
        return usb_cdc.data.read(size)
  
    def close(self):
        if self.ser:
            self.ser.close()
            
    def pyif_data(self) -> bool:
        return self.ser.in_waiting > 0
    
    def cirpyif_data(self) -> bool:
        return usb_cdc.data.in_waiting > 0

#------------------------------------------------------------------------#
