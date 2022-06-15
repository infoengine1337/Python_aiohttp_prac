import asyncio
import aiohttp
import time

async def donate_ukraine():

    dest_url = "http://localhost:8080"
    async with aiohttp.ClientSession() as session:
        for i in range(1000):
            async with session.get(dest_url) as response:
                print("Status:", response.status)


def main():
    start = time.time()
    asyncio.run(donate_ukraine())
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

if __name__ == '__main__':
    main()
