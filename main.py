import asyncio
import aiohttp
import time

async def poipoi(session, url):
    async with session.get(url) as resp:
        text = resp.text
        return text


async def donate_ukraine():

    dest_url = "http://localhost:8080"

    async with aiohttp.ClientSession() as session:
        tasks = []

        for i in range(10000):
            tasks.append(asyncio.create_task(poipoi(session, dest_url)))
        
        return_lists = await asyncio.gather(*tasks)

def main():
    start = time.time()
    asyncio.run(donate_ukraine())
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")

if __name__ == '__main__':
    main()
