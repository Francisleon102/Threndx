import asyncio as aio

async def incoming():
    while True:
        print("Incoming message")
        await aio.sleep(1)