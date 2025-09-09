from modules import mqtt
from modules import wifi

if __name__ == "__main__":
    if wifi.connect():
        print("Wi-Fi connection established.")

        client = mqtt.connect()

        if client:
            mqtt.publish_and_wait(client)
        else:
            print("Could not connect to MQTT broker.")
    else:
        print("Wi-Fi connection failed. Cannot proceed with MQTT.")
