# Library used to communicate with arduino storage cart
# Written by Michael Lance
# Created: 5/31/2024
# Last Modified: 06/01/2024
#---------------------------------------------------------------------------------------------------#

import sys
import time
from serwrap import *
import struct

if sys.implementation.name != 'circuitpython':
    digitalio = None
elif sys.implementation.name == 'circuitpython':
    candyserial = None
    import digitalio
    
#---------------------------------------------------------------------------------------------------#
"""
Oh boy its that candycom 2.0 without asyncio to allow that to be your choice!
"""
#---------------------------------------------------------------------------------------------------#

class CommAgent:
    def __init__ (self):
        self.ser = SerHandler(9600)
    
    def read(self, size):
        data = self.ser.read(size)
        return data
    
    def _read_exactly(self, size):
        data = bytearray()
        while len(data) < size:
            packet = self.read(size - len(data))
            if not packet:
                return None
            data.extend(packet)
        return bytes(data)
    
    def read_message(self):
        # Read the header first
        header = self._read_exactly(Message.HEADER_SIZE)
        if not header:
            return None
        message_type_code, payload_length = struct.unpack(Message.HEADER_FORMAT, header)
        
        # Now read the payload based on the length in the header
        payload = self._read_exactly(payload_length)
        if not payload:
            return None
        
        # Combine header and payload to unpack the full message
        full_message = header + payload
        
       
        return Message.unpack(full_message)
    
    
    def print_payload(self):
        message_obj = self.read_message()
        print(message_obj.payload)
    
    def return_payload(self):
        message_obj = self.read_message()
        return message_obj.payload
        
    def write(self, payload):
        """
        Write a message to the serial buffer.

        Args:
            message_type (str): Type of the message ('int' or 'str').
            payload (int or str): The payload of the message.
        """
        
        if type(payload) == int:
            message_type = "int"
        elif type(payload) == str:
            message_type = "str"
        else:
            print("un supported message type")
            return None
        
        message = Message(message_type, payload)
        packed_message = message.pack()
        if packed_message:
            self.ser.write(packed_message)
        else:
            print("Error: Failed to pack the message.")
            
    def if_data(self) -> bool:
        return self.ser.if_data()

class Message:
    HEADER_FORMAT = 'BH'  # Combined format without spaces
    try:
        HEADER_SIZE = struct.calcsize(HEADER_FORMAT)  # Calculate header size
    except Exception as e:
        print(f"Error calculating HEADER_SIZE with format {HEADER_FORMAT}: {e}")

    def __init__(self, message_type, payload):
        self.message_type = message_type
        self.payload = payload
        
        # Determine payload format and length based on message type and payload
        if message_type == 'int' and isinstance(payload, int):
            self.payload_format = 'I'  # Unsigned integer (4 bytes)
            self.payload_length = struct.calcsize('I')
        elif message_type == 'str' and isinstance(payload, str):
            self.payload = payload.encode('utf-8')  # Encode string to bytes
            self.payload_format = f'{len(self.payload)}s'  # String format
            self.payload_length = len(self.payload)
        else:
            raise ValueError("Invalid payload type for the given message type.")
        
        self.message_format = f'BH{self.payload_format}'  # Combined format without space

    def pack(self):
        # Pack the header and payload into a binary format
        try:
            packed_message = struct.pack(self.message_format, 
                                         1 if self.message_type == 'int' else 2, 
                                         self.payload_length, 
                                         self.payload)
            return packed_message
        except struct.error as e:
            print(f"Error packing message: {e}")
            return None

    @staticmethod
    def unpack(data):
        try:
            # Unpack the header to get the message type and payload length
            header = data[:Message.HEADER_SIZE]
            message_type_code, payload_length = struct.unpack(Message.HEADER_FORMAT, header)
        except struct.error as e:
            print(f"Error unpacking header: {e}")
            return None
        
        # Determine the format of the payload based on the message type
        if message_type_code == 1:  # Integer
            payload_format = 'I'
            message_type = 'int'
        elif message_type_code == 2:  # String
            payload_format = f'{payload_length}s'
            message_type = 'str'
        else:
            print("Invalid message type.")
            return None
        
        message_format = f'BH{payload_format}'  # Combined format without space
        
        try:
            # Unpack the entire message using the determined format
            message_data = data[:Message.HEADER_SIZE + payload_length]
            unpacked_data = struct.unpack(message_format, message_data)
        except struct.error as e:
            print(f"Error unpacking message: {e}")
            return None
        
        # Extract and decode the payload if it's a string
        payload = unpacked_data[2]
        if message_type == 'str':
            payload = payload.decode('utf-8')
        
        return Message(message_type, payload)

    def __str__(self):
        return f'Message(type={self.message_type}, length={self.payload_length}, payload={self.payload})'
#---------------------------------------------------------------------------------------------------#