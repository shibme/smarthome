# SmartHome Scripts

This codebase is for maintaining all my smarthome-related scripts.

## Heatrick

- The script in this repository is `heatrick/run.py` is used to control a TP-Link smart plug.
- The script discovers the device on the network, checks its status, and toggles it on and off in a loop.
- The purpose of this is to run it during power outage and trick the backup supply meter to believe that my apartment's load is under limits (the backup supply meter checks every 5 seconds).

### Usage

To run the script, ensure you have the required environment variables set:

- `SMARTHOME_DEVIDE_IP_ADDRESS`: The IP address of the TP-Link device.
- `SMARTHOME_TPLINK_USERNAME`: The username for the TP-Link device.
- `SMARTHOME_TPLINK_PASSWORD`: The password for the TP-Link device.

You can set these variables in your shell before running the script:

```sh
export SMARTHOME_DEVIDE_IP_ADDRESS="your_device_ip"
export SMARTHOME_TPLINK_USERNAME="your_username"
export SMARTHOME_TPLINK_PASSWORD="your_password"
```

Then, run the script using Python:

```sh
python heatrick/run.py
```