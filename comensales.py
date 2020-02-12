import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaphore = threading.Semaphore(0)
lock = threading.Lock()

class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    while (True):
      semaphore.acquire()   
      logging.info('Reponiendo los platos...')
      platosDisponibles = 3

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = f'Comensal {numero}'

  def run(self):
    global platosDisponibles
    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    if platosDisponibles == 0:
      semaphore.release()
      Cocinero().start()
    else:
      semaphore.acquire()
      

platosDisponibles = 3


#Cocinero().start()

for i in range(5):
  try:
    Comensal(i).start()
    lock.acquire()
  finally:
    lock.release()

  

