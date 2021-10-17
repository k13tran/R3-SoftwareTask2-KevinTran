# Program which receives input from a client which is used to
# control the movement and speed of the rover where movement is
# controlled by "wasd" and speed is controlled by numerical inputs
# from 0 to 5 (where 0 is the lowest speed setting and 5 is the
# highest speed setting)
#
# Kevin Tran

import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)
data = b''
speed = 0               # The current speed mode of the rover
wheels = [0, 0, 0, 0]   # The current speed configuration for each wheel

# Just to check if it's working
print("Server online")


# For the functions below, each index represents the motor for each wheel
# i.e. wheels[0] = M1, wheels[1] = M2, ...
# The mapping is based on figure 4 in the software training package 2


# Stop all wheels
def stop():
    set_wheels = [0, 0, 0, 0]
    return set_wheels


# Move all wheels forward
def forward(current_speed):
    set_wheels = [current_speed, current_speed, current_speed, current_speed]
    return set_wheels


# Move all wheels backward
def backward(current_speed):
    set_wheels = [current_speed, current_speed, current_speed, current_speed]
    return set_wheels


# Move right wheels backward, left wheels forward
def turn_left(current_speed):
    set_wheels = [-current_speed, -current_speed, current_speed, current_speed]
    return set_wheels


# Move right wheels forward, left wheels backward
def turn_right(current_speed):
    set_wheels = [current_speed, current_speed, -current_speed, -current_speed]
    return set_wheels


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)

        # Server closes on input "f" and sends the input back before closing
        while data.decode('UTF-8') != 'f':
            data = conn.recv(1024)

            # Code below determines settings for movement (where input "wasd"
            # is used to control direction of movement) and speed (from input
            # "0" for no movement to input "5" for the fastest speed setting)
            if data.decode('UTF-8') == "stop":
                wheels = stop()
                print(wheels)
            elif data.decode('UTF-8') == 'w':
                wheels = forward(speed)
                print(wheels)
            elif data.decode('UTF-8') == 'a':
                wheels = turn_left(speed)
                print(wheels)
            elif data.decode('UTF-8') == 's':
                wheels = backward(speed)
                print(wheels)
            elif data.decode('UTF-8') == 'd':
                wheels = turn_right(speed)
                print(wheels)
            elif data.decode('UTF-8') == '0':
                speed = 0
            elif data.decode('UTF-8') == '1':
                speed = 51
            elif data.decode('UTF-8') == '2':
                speed = 102
            elif data.decode('UTF-8') == '3':
                speed = 153
            elif data.decode('UTF-8') == '4':
                speed = 204
            elif data.decode('UTF-8') == '5':
                speed = 255
