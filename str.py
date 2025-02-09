import asyncio
from pyrogram import Client

print("Enter your app information from my.telegram.org/apps below.")

async def main():
    api_id = 14964504  # Your API ID
    api_hash = "7ddc2e405de3b79daa752d971f3336b8"  # Your API Hash

    # Create a temporary client session and export the session string
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        print(await app.export_session_string())  # This will print the session string

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
