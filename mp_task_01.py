import threading
import time
import multiprocessing
import math
import requests

# список url
urls = ['https://www.example.com'] * 10


def fetch_url(url):
    response = requests.get(url)
    return response.text


def sequence():
    # время старта start_time
    start_time = time.time()

    # выполнение функции fetch_url для каждого url из urls
    [fetch_url(url) for url in urls]

    # время окончания end_time
    end_time = time.time()
    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    # время старта start_time
    start_time = time.time()
    # выполнение с помощью потоков функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех потоков)
    # Создаем и запускаем потоки для каждого URL
    threads_list = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))

        threads_list.append(thread)
        thread.start()

    # Ждем завершения всех потоков
    for thread in threads_list:
        thread.join()

    # время окончания end_time
    end_time = time.time()
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    # время старта start_time
    # выполнение с помощью процессов функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех процессов)
    # время окончания end_time
    print(f'processes time: {end_time - start_time: 0.2f} \n')

def processes():
    # время старта start_time
    start_time = time.time()  # время старта

    # выполнение с помощью процессов функции fetch_url для каждого url из urls (с ожиданием окончания выполнения всех процессов)
    # Создаем процессы для каждого URL
    processes_list = []
    for url in urls:
        process = multiprocessing.Process(target=fetch_url, args=(url,))
        processes_list.append(process)
        process.start()  # Запускаем процесс

    # Ждем завершения всех процессов
    for process in processes_list:
        process.join()

    # время окончания end_time
    end_time = time.time()  # время окончания
    print(f'processes time: {end_time - start_time:0.2f} seconds\n')


if __name__ == '__main__':
    from mp_task_01_asyncio import asyncio, asyncio_f

    sequence()
    threads()
    processes()
    asyncio.run(asyncio_f())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        sequence time:  ???

        threads time:  ???
        
        processes time:  ???
    """
