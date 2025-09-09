## Hardware setup for docker development container

Before launching the dev container, you must perform a one-time setup on your host machine to grant the container access to the USB serial ports.

### Linux

You need to add your user account to the `dialout` group, which has permission to access serial devices.

1.  Run the following command in your terminal:
    ```bash
    sudo usermod -aG dialout $USER
    ```
2.  **Important:** You must **log out and log back in** for this change to take effect.
3.  After logging back in, you can uncomment the Linux line in the `.devcontainer/devcontainer.json` file.

### Windows

On Windows, you must use the `usbipd-win` tool to forward your ESP32 from the Windows host to the WSL 2 environment where Docker runs.

1.  Open **PowerShell as an Administrator**.
2.  Install `usbipd-win` (if you haven't already):

    ```powershell
    winget install --interactive --exact dorssel.usbipd-win
    ```

3.  Plug in your ESP32 and run the following commands in your Admin PowerShell:

    ```powershell
    # List devices to find the BUSID of your ESP32
    usbipd wsl list

    # Attach the device to WSL, replacing <BUSID> with the ID from the list
    usbipd wsl attach --busid <BUSID>
    ```

    **Note:** This `attach` command must be run each time you plug in the device or restart your computer. No changes are needed in the `devcontainer.json` file.

### macOS

No special prerequisite steps are required on macOS. Docker Desktop is already configured to handle device mapping.

1.  Simply uncomment the macOS line in the `.devcontainer/devcontainer.json` file.

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

[micropython library]
