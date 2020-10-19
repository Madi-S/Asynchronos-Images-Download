import asyncio
import aiohttp
from time import time, sleep


import sys


def write_img(data):
    filename = f'file_{len(data)}.jpg'
    with open(filename, 'wb') as f:
        f.write(data)
        print(len(data), 'wrote')


async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_img(data)


async def main():
    url = 'https://loremflickr.com/320/240/dog'
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            task = asyncio.create_task(fetch_content(url, session))
            tasks.append(task)

        await asyncio.gather(*tasks)

    sleep(0.5)

if __name__ == '__main__':
    t1 = time()
    asyncio.run(main())
    print(time()-t1)
