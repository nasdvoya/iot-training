# Configuration

PORT := "/dev/cu.usbserial-0001"
FIRMWARE := "ESP32_GENERIC-20250911-v1.26.1.bin"
BAUD := "460800"

# List serial ports (macOS / Linux)
find-port:
    @echo "macOS:"
    @ls /dev/cu.usb* 2>/dev/null || true
    @echo ""
    @echo "Linux:"
    @ls /dev/ttyUSB* /dev/ttyACM* 2>/dev/null || true
    @echo ""
    @echo "Windows (PowerShell):"
    @echo "  Get-CimInstance -ClassName Win32_SerialPort"

# Erase and flash MicroPython firmware
flash:
    esptool --port {{ PORT }} erase-flash
    esptool --port {{ PORT }} --baud {{ BAUD }} write-flash -z 0x1000 {{ FIRMWARE }}

# Open REPL with rshell. Press "CTRL+X" to leave repl and rshell.
repl:
    rshell -p {{ PORT }} repl

# Upload a single file
upload file:
    rshell -p {{ PORT }} cp {{ file }} /pyboard/

# Upload a directory recursively
upload-dir dir:
    rshell -p {{ PORT }} rsync {{ dir }}/ /pyboard/{{ dir }}/

# Open rshell file system shell. Type "exit" to quit rshell.
fs:
    rshell -p {{ PORT }}

# Full flash erase only
erase:
    esptool --port {{ PORT }} erase-flash
