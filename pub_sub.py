import asyncio
from nats.aio.client import Client as NATS

async def subscribe_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received a message on '{subject}': {data}")

async def run():
    nc = NATS()

    await nc.connect(servers=["nats://127.0.0.1:4222"])

    subscription = await nc.subscribe("updates", cb=subscribe_handler)

    await nc.publish("updates", b'Hello, this is the first message!')
    await nc.publish("updates", b'Another update from the NATS publisher')

    await asyncio.sleep(2)

    # Unsubscribe from the subject
    await subscription.unsubscribe()

    # Close the connection
    await nc.close()

if __name__ == "__main__":
    # Run the async function
    asyncio.run(run())
