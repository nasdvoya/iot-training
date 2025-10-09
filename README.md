## ESP32 Training

### Development environment and tools

[uv](https://github.com/astral-sh/uv)
[esptool](https://github.com/espressif/esptool)
[just](https://github.com/casey/just)

### Code

```bash
Create virtual environment
uv venv
source .venv/bin/activate
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
