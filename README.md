## Hardware setup for docker development container

### Development environment

[Install uv](https://github.com/astral-sh/uv)

```bash
Create virtual environment
uv venv
source .venv/bin/activate
```

### Workflow - Cheatsheet

```bash
## find port
# macos
ls /dev/cu.usb*
# linux
ls /dev/ttyusb*
# windows, powershell
get-ciminstance -classname win32_serialport
```

```bash
## flash
# erase
esptool --port <your_port> erase-flash
# flash new firmware
esptool --port <your_port> --baud 460800 write-flash 0x1000 firmware.bin
```

```bash
## --- rshell and repl
# rshell session
rshell -p <your_port>
# rshell session with repl
rshell -p <your_port> repl
#Control-D: Perform a soft reboot to run your new main.py.
#Control-C: Stop a running script.
#Control-X: Exit the REPL (returns you to your normal terminal).

# #--- repl - working with a project

# --- you are now in the rshell prompt ---

# copy your files and directories to the board's root (/pyboard/)
cp -r lib/ /pyboard/
cp -r examples/ /pyboard/
cp boot.py /pyboard/
cp main.py /pyboard/
cp secrets.py /pyboard/

# exit rshell (in rshell)
exit

```

### Packages

[micropython-lib](https://github.com/micropython/micropython-lib/tree/master)
[Package index](https://micropython.org/pi/v2/index.json)

#### python-stdlib

Standard library modules, included in the MicroPython firmware.

> json, time, os, struct, sys, random, asyncio, array, io

#### python-ecosys

"Simplified" version of common PyPi packages.

> aiohttp, uasyncio, urequests

#### micropython

Micropython specific packages.

> lora, bluetooth, espflash, mip

#### unix-ffi

Used to interact with host OS libraries or FFI (Foreign Function Interface)
