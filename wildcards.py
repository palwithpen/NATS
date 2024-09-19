import asyncio
from nats.aio.client import Client as NATS

# Handler function to process messages
async def subscribe_handler(msg):
    subject = msg.subject
    data = msg.data.decode()
    print(f"Received a message on '{subject}': {data}")

async def run():
    # Create a new NATS client instance
    nc = NATS()

    # Connect to the NATS server
    await nc.connect(servers=["nats://127.0.0.1:4222"])

    # Subscribe using the single-level wildcard (*)
    await nc.subscribe("foo.*.bar", cb=subscribe_handler)

    # Subscribe using the multi-level wildcard (>)
    await nc.subscribe("foo.>", cb=subscribe_handler)

    # Publish to different subjects to test the wildcard subscriptions
    await nc.publish("foo.a.bar", b"Message for foo.a.bar")
    await nc.publish("foo.b.bar", b"Message for foo.b.bar")
    await nc.publish("foo.a.b", b"Message for foo.a.b")
    await nc.publish("foo.x.y.z", b"Message for foo.x.y.z")

    # Optionally, wait a bit to ensure messages are received
    await asyncio.sleep(2)

    # Close the connection
    await nc.close()

if __name__ == "__main__":
    # Run the async function
    asyncio.run(run())
