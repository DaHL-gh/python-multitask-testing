import asyncio
import time
import math

from mp_task_02 import fibonacci, trapezoidal_rule

async def compute_fibonacci(loop):
    return await loop.run_in_executor(None, fibonacci, 700003)

async def compute_trapezoidal_rule(loop):
    return await loop.run_in_executor(None, trapezoidal_rule, math.sin, 0, math.pi, 20000000)

async def asyncio_f():
    # время старта start_time
    start_time = time.time()  # время старта

    loop = asyncio.get_running_loop()
    fib_task = asyncio.create_task(compute_fibonacci(loop))
    trap_task = asyncio.create_task(compute_trapezoidal_rule(loop))

    await asyncio.gather(fib_task, trap_task)  # Ожидание завершения всех задач

    # время окончания end_time
    end_time = time.time()  # время окончания
    print(f'asyncio time: {end_time - start_time:0.2f} seconds\n')

if __name__ == '__main__':
    asyncio.run(asyncio_f())