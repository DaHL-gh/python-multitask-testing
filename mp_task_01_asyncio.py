import asyncio
import time
import aiohttp

urls = ['https://www.example.com'] * 10

# Пример асинхронной функции fetch_url
async def fetch_url(session, url):
    async with session.get(url) as response:
        await response.text()

async def asyncio_f():
    # время старта start_time
    start_time = time.time()  # время старта

    # асинхронное выполнение запросов
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(fetch_url(session, url) for url in urls))  # Ожидание завершения всех задач

    # время окончания end_time
    end_time = time.time()  # время окончания
    print(f'asyncio time: {end_time - start_time:0.2f} seconds\n')

if __name__ == '__main__':
    asyncio.run(asyncio_f())
