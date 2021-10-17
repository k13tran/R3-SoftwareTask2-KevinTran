# Program for sending instructions to the server which ends
# when input "f" is echoed from the server
#
# Kevin Tran

from pynput import keyboard
import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
data = b''


# Send the keypress to the server as soon as they are pressed
def on_press(key):
    try:
        s.sendall(bytes(key.char, 'utf-8'))
    except AttributeError:
        pass


listener = keyboard.Listener(on_press=on_press)
listener.start()

# Just to check if it's working
print("Client Online")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Client closes on input "f" as received from the server
    while data != b'f':
        data = s.recv(1024)