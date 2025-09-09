import time
from umqtt.robust import MQTTClient
import machine
import ubinascii
import os

MQTT_BROKER_HOST = "192.168.0.60"
MQTT_PORT = 1883


def sub_cb(topic, msg):
    print(f"Received message on topic: {topic.decode()}")
    print(f"Message: {msg.decode()}")


def connect():
    try:
        unique_id = machine.unique_id()
        if unique_id:
            client_id = ubinascii.hexlify(unique_id).decode()
        else:
            client_id = ubinascii.hexlify(os.urandom(8)).decode()
            print("Warning: Using a random client ID as machine.unique_id() is empty.")

        client = MQTTClient(
            client_id=client_id, server=MQTT_BROKER_HOST, port=MQTT_PORT
        )

        client.set_callback(sub_cb)

        print(
            f"Attempting to connect to MQTT broker at {MQTT_BROKER_HOST}:{MQTT_PORT}..."
        )
        if not client.connect(clean_session=True):
            print("Connected to MQTT broker.")
            # Subscribe to the 'foo_topic' to receive messages
            client.subscribe(b"foo_topic")
            print("Subscribed to 'foo_topic'")
            return client
        else:
            print("Failed to connect to MQTT broker.")
            return None

    except Exception as e:
        print(f"An error occurred during MQTT connection: {e}")
        return None


def publish_and_wait(client):
    try:
        counter = 0
        while True:
            # Check for any incoming messages from subscribed topics
            client.check_msg()

            message = f"Hello from MicroPython, message count: {counter}"
            client.publish(b"bar_topic", message.encode())
            print(f"Published to 'bar_topic': {message}")

            counter += 1

            time.sleep(5)
    except KeyboardInterrupt:
        print("Interrupted by user, disconnecting...")
    except Exception as e:
        print(f"An error occurred during the main loop: {e}")
    finally:
        if client:
            client.disconnect()
            print("Disconnected from MQTT broker.")
