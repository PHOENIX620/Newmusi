import asyncio
from pyrogram import Client

print("Enter your app information from my.telegram.org/apps below.")

async def main():
    api_id = 14964504  # Your API ID
    api_hash = "7ddc2e405de3b79daa752d971f3336b8"  # Your API Hash
    session_string = "BQDkVxgAVByicTqSuqnkTwrIFXhJLvMJ2pGwpPBP41HKkZuctVup5H-qR-IKxTxmT8jzIlhBYn4WWM_ZdBmroWAKBXxGSxstT5aTqupiN4KbYPj389PgMml4jSdosEq-HKM5j7_1azHDzhIYqnGiwX33FMGOQIRTIcLRwfa5NzFF7OqNZeZKLrGcDvbVX4iu62AezsHt3jATF6mVCs5Me2Yscr5a9auRQJ26rZM__NyeSte82BwywUxD0KndBE_sHNZeTn-w3csdaKO5rhC61A5CaDe00zgbFHjha74w2atXi0jrSu7DrUJdz37N0NibLdG8W3bncfY-ekEVZjuV52dJwrc2_wAAAAHOQYzfAA"  # Your session string

    # Create a client session with the provided session string
    async with Client(session_string, api_id=api_id, api_hash=api_hash) as app:
        print("Session started successfully!")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
