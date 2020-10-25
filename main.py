import asyncio
import aiohttp
from time import time, sleep
from uuid import uuid4



# Synchronous function to write images
def write_img(data):
    filename = f'file_{uuid4()}.jpg'  # Creating probably unique filename
    with open(filename, 'wb') as f:
        f.write(data)
        print(len(data), 'wrote')

# Asynchronous function to retrieve the data of the response 
async def fetch_content(url, session):
    async with session.get(url, allow_redirects=True) as response: # Using GET method to get the response
        data = await response.read()  # Reading response to retrieve data
        write_img(data) # Calling synchronous function to write images

# Asynchronous main function to create tasks and execute them
async def main():
    url = 'https://loremflickr.com/320/240/dog' # URL, which generates random image every time. It can be replaced with lists of URLs to parse
    tasks = []  # Empty tasks list

    async with aiohttp.ClientSession() as session:  # Creating asynchronous session using aiohttp
        for _ in range(500):  # Can be replaced with: for url in urls (if lists of urls is used)
            task = asyncio.create_task(fetch_content(url, session))  # Creating task by passing function with its arguments
            tasks.append(task)  # Appending the task to tasks list

        await asyncio.gather(*tasks)  # Unpack tasks - [task1,task2,task3] becomes task1,task,task3 ~ multiple arguments instead of a single one

    sleep(1.5) # Sleeping to avoid RunTime Error (works for Windows)

if __name__ == '__main__': # If the file was called directly
    t1 = time()  # Start time
    asyncio.run(main()) # Executing main function
    print(time()-t1) # Measuring start_time - finish_time
