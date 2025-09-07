# This script runs on boot-up, before main.py
import webrepl
import gc

# Start the WebREPL daemon
webrepl.start()
print("WebREPL started on boot")

gc.collect()