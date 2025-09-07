from modules import wifi

if wifi.connect():
    print("Wi-Fi connection established.")
else:
    print("Wi-Fi connection failed.")
