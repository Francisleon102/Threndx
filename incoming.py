import asyncio
import websockets
import base64
import json

# Alpaca API Credentials


KEY_ID = "PKYBD9IQOMHV4NNNANLC"
SECRET = "Vn5NJazAldHMKxs9Q8byj453AzhPogPxCHPdtoJK"

# WebSocket URL
WS_URL = "wss://stream.data.alpaca.markets/v2/test"

# Encode authentication for Broker API (if needed)
auth_header = base64.b64encode(f"{KEY_ID}:{SECRET}".encode()).decode()

async def connect_ws():
    async with websockets.connect(WS_URL) as ws:
        # Authenticate
        auth_data = {
            "action": "auth",
            "key": KEY_ID,
            "secret": SECRET
        }
        await ws.send(json.dumps(auth_data))
        response = await ws.recv()
        print(f"Auth Response: {response}")

        # Subscribe to a channel (example: trade updates)
        sub_data = {
            "action": "subscribe",
            "trades": ["AAPL"]  # Change symbol as needed
        }
        await ws.send(json.dumps(sub_data))
        response = await ws.recv()
        print(f"Subscription Response: {response}")

        # Listen for messages
        while True:
            message = await ws.recv()
            print(f"Message Received: {message}")

# Run the WebSocket client

