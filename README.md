### By Kevin Tran

# R3 - Software Task 2

For the project, I created two python files as outlined in the package where for the program, input.py
(client), sends instructions to output.py (server). Overall, the client detects input from the keyboard
which is then sent to the server where it is decoded into instructions as to how the rover should move.

## input.py

The program detects input from the keyboard and sends it to the server and also detects when the key is
released which is sent to the server as well (explained later). The program only deals with collecting
input from the user where the program ends upon input "f" is echoed from the server.

## output.py

The program receives instructions from the client which are then decoded into instructions as to how
the rover should move. For the speed setting, it takes a numerical input from 0 to 5 (where 0 is 
the slowest speed setting (doesn't move) and 5 is the fastest speed setting). For directional inputs,
it is based around the "wasd" keys where "w" is to move forward, "a" is to move left, etc. However,
upon detecting the string "stop" (which occurs when the key is released), the rover stops moving. The
server also ends upon input "f" which is echoed back to the client before the program closes.

## Appendix

![Alt text](https://i.gyazo.com/00190fd63a9ffe51f32beb9afa364653.png)
<br />
A1: Moving forward and stopping (Green text is input)

![Alt text](https://i.gyazo.com/6e697f0f68e1e9ad47c8c353bf0bd2a1.png)
<br />
A2: Changing speed and moving left (Green text is input)
