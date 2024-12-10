import socket
import numpy as np
import velodyne_decoder as vd
import time
import struct



# Configuration settings
LIDAR_IP = "192.168.1.201"
LIDAR_PORT = 2368

# Create a socket to receive data from the LiDAR
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', LIDAR_PORT))

# Initialize the Velodyne decoder
config = vd.Config(model=vd.Model.VLP16)
decoder = vd.ScanDecoder(config)

print(f"Listening for data from {LIDAR_IP} on port {LIDAR_PORT}")
n =1
try:
    while True:
        data, addr = sock.recvfrom(1248)  # Velodyne data packets are typically 1206 bytes
        #data = vd.PacketVector(data)
        if addr[0] == LIDAR_IP:
            # Decode the packet to a point cloud
            # Print the received data
            print(f"Received data from {addr}: {data.decode('utf-8')}")
            time.sleep(1)
            # Here, you can further process the point cloud data, e.g., save to a file, visualize, etc.

except KeyboardInterrupt:
    print("Stopping data capture.")

finally:
    sock.close()
    print("Socket closed.")
