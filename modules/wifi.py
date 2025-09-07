import network
import time
import secrets

wlan = network.WLAN(network.STA_IF)


def connect():
    """
    Activates the WLAN interface and connects to the network.
    Includes a timeout.
    Returns:
        bool: True on success, False on failure.
    """
    if wlan.isconnected():
        print("Wi-Fi already connected.")
        return True

    print("Connecting to Wi-Fi...")
    wlan.active(True)
    wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASS)  # type: ignore

    # Wait for connection with a 10-second timeout
    max_wait = 10
    while max_wait > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        max_wait -= 1
        print(".", end="")
        time.sleep(1)

    # Handle connection success or failure
    if wlan.isconnected():
        print("\nConnected! IP:", wlan.ifconfig()[0])
        return True
    else:
        print("\nFailed to connect.")
        return False
