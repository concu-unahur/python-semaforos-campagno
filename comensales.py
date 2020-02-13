import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaphore = threading.Semaphore(0)
semaphore2 = threading.Semaphore(1)


class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    global semaphore
    global semaphore2
    while (True):   
      semaphore.acquire()
      logging.info('Reponiendo los platos...')
      platosDisponibles = 3
      semaphore2.release()
      

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    global semaphore
    global semaphore2
    semaphore2.acquire()
    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    if platosDisponibles == 0:
      semaphore.release()
    else:
      #semaphore.acquire()
      semaphore2.release()
      

platosDisponibles = 3


Cocinero().start()

for i in range(10):
    Comensal(i).start()

  

