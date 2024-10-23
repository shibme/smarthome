import asyncio
import os
from kasa import Discover

async def main():
    # get ip address from environment variable
    device_ip_address = os.environ.get("SMARTHOME_DEVIDE_IP_ADDRESS")
    tplink_username = os.environ.get("SMARTHOME_TPLINK_USERNAME")
    tplink_password = os.environ.get("SMARTHOME_TPLINK_PASSWORD")
    dev = await Discover.discover_single(device_ip_address,username=tplink_username,password=tplink_password)
    await dev.update()
    if dev.is_on:
        print("Device is on, turning off")
        await dev.turn_off()
        await asyncio.sleep(2)
    count = 0
    while True:
        count += 1
        print(f"Iteration: {count}")
        await dev.turn_on()
        await asyncio.sleep(3)
        await dev.turn_off()
        await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())