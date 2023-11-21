import time
import logging

from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')

def super_task(a, b):
    time.sleep(1)
    logging.info(f'Terminamos la tarea compleja!! con valores {a} {b}\n')

if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    # recibe la funcion y sus parametros de entrada
    executor.submit(super_task,10,20)
    executor.submit(super_task, 5, 20)
    executor.submit(super_task, 15, 50)