import serial
import struct
import time

# Calculate CRC-16 for Modbus RTU
def modbus_crc(data):
    crc = 0xFFFF
    for pos in data:
        crc ^= pos
        for _ in range(8):
            if (crc & 1):
                crc >>= 1
                crc ^= 0xA001
            else:
                crc >>= 1
    return crc

# Build request frame to read 2 registers: humidity & temperature
def build_request(slave_id=0x01, reg_start=0x0000, reg_count=0x0002):
    frame = bytearray([
        slave_id,
        0x03,  # Function Code: Read Holding Register
        reg_start >> 8, reg_start & 0xFF,
        reg_count >> 8, reg_count & 0xFF
    ])
    crc = modbus_crc(frame)
    frame.append(crc & 0xFF)
    frame.append((crc >> 8) & 0xFF)
    return frame


# Configure serial port (update if needed)
ser = serial.Serial(
    port="/dev/ttyACM0",  # Change according to your system
    baudrate=9600,
    bytesize=8,
    parity="N",
    stopbits=1,
    timeout=1
)

request = build_request()

try:
    while True:
        ser.write(request)
        time.sleep(0.1)
        response = ser.read(9)

        if len(response) >= 7:
            humidity = struct.unpack(">H", response[3:5])[0] / 10.0
            temperature = struct.unpack(">H", response[5:7])[0] / 10.0

            print(f"Humidity   : {humidity:.1f} %RH")
            print(f"Temperature: {temperature:.1f} °C")
        else:
            print("Warning: Insufficient data received.")

        time.sleep(1)  # Delay between readings

except KeyboardInterrupt:
    print("User stopped the program. Exiting...")

except Exception as e:
    print("Error occurred:", e)

finally:
    ser.close()
