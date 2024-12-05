import threading
import time
import multiprocessing
import math


# Функции для АТ-03

# запускать с n = 700003
def fibonacci(n):  # содержимое функции не менять
    """Возвращает последнюю цифру n-е числа Фибоначчи."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    print(f'fibonacci = {b % 10}')


# запускать с f, a, b, n равными соответственно math.sin, 0, math.pi, 20000000
def trapezoidal_rule(f, a, b, n):  # содержимое функции не менять
    """Вычисляет определенный интеграл функции f от a до b методом трапеций с n шагами."""
    h = (b - a) / n
    integral = (f(a) + f(b)) / 2.0
    for i in range(1, n):
        integral += f(a + i * h)
    print(f'trapezoidal_rule = {integral * h}')


def sequence():
    # время старта start_time
    start_time = time.time()

    # вычисление fibonacci от значения 700003
    fibonacci(700003)

    # вычисление trapezoidal_rule со значениями math.sin, 0, math.pi, 20000000
    trapezoidal_rule(math.sin, 0, math.pi, 20000000)

    # время окончания end_time
    end_time = time.time()

    print(f'sequence time: {end_time - start_time: 0.2f} \n')


def threads():
    # время старта start_time
    start_time = time.time()

    # вычисления на потоках:
    # Создаем потоки
    fib_thread = threading.Thread(target=fibonacci, args=(700003,))
    trap_thread = threading.Thread(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))

    # Запускаем потоки
    fib_thread.start()
    trap_thread.start()

    # Ждем завершения потоков
    fib_thread.join()
    trap_thread.join()

    # время окончания end_time
    end_time = time.time()
    print(f'threads time: {end_time - start_time: 0.2f} \n')


def processes():
    # время старта start_time
    start_time = time.time()

    # вычисления на процессах:
    # Создаем процессы
    fib_process = multiprocessing.Process(target=fibonacci, args=(700003,))
    trap_process = multiprocessing.Process(target=trapezoidal_rule, args=(math.sin, 0, math.pi, 20000000))

    # Запускаем процессы
    fib_process.start()
    trap_process.start()

    # Ждем завершения процессов
    fib_process.join()
    trap_process.join()

    # время окончания end_time
    end_time = time.time()
    print(f'processes time: {end_time - start_time: 0.2f} \n')


if __name__ == '__main__':
    from mp_task_02_asyncio import asyncio, asyncio_f

    sequence()
    threads()
    processes()
    asyncio.run(asyncio_f())
    """
        Результатом должно стать (знаки вопроса заменятся на ваше время выполнения):
        
        fibonacci = 7
        trapezoidal_rule = 2.000000000000087
        sequence time:  ???
        
        fibonacci = 7
        trapezoidal_rule = 2.000000000000087
        threads time:  ??? 
        
        fibonacci = 7
        trapezoidal_rule = 2.000000000000087
        processes time:  ???
    """
