import asyncio
from nats.aio.client import Client as NATS
import async_timeout

async def check_nats_connection():
    nc = NATS()

    try:
        # Use async_timeout to handle the timeout for connection
        async with async_timeout.timeout(2):
            await nc.connect(servers=["nats://192.168.1.11:4222"])
            print("Connected to NATS server!")
        
        # Close the connection once connected
        await nc.close()
    except asyncio.TimeoutError:
        print("Connection attempt timed out.")
    except Exception as e:
        print(f"Failed to connect to NATS: {e}")

if __name__ == "__main__":
    # Run the async function to check connection
    asyncio.run(check_nats_connection())
