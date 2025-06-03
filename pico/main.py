from connections import connect_mqtt, connect_internet
from time import sleep
from constants import ssid, mqtt_server, mqtt_user, mqtt_pass
from motortest2 import move_forward, move_backward, turn_left, turn_right, stop


# Function to handle an incoming message

def cb(topic, msg):

    if topic == b"direction":
        if msg == b"forward":
            print("Forward")
            move_forward()
            sleep(0.001)
        elif msg == b"backward":
            move_backward()
            sleep(0.001)
        elif msg == b"left":
            turn_left()
            sleep(0.001)
        elif msg == b"right":
            turn_right()
            sleep(0.001)
        elif msg == b"stop":
            print("Stop")
            stop()
            sleep(0.001)
        
            
            


def main():
    try:
        connect_internet("HAcK-Project-WiFi-2",password="UCLA.HAcK.2024.Summer")
        client = connect_mqtt("cabab558654e453d9b25d76f57219102.s1.eu.hivemq.cloud", "picow", "Fun1234!")

        client.set_callback(cb)
        client.subscribe("direction")
        while True:
            client.check_msg()
            sleep(1)
    except KeyboardInterrupt:
        print('keyboard interrupt')
        
        
if __name__ == "__main__":
    main()

