import threading
import time
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S', level=logging.INFO)

semaCocinero = threading.Semaphore(0)
semaComensal = threading.Semaphore(1)


class Cocinero(threading.Thread):
  def __init__(self):
    super().__init__()
    self.name = 'Cocinero'

  def run(self):
    global platosDisponibles
    global semaCocinero
    global semaComensal
    while (True):   
      semaCocinero.acquire()
      logging.info('Reponiendo los platos...')
      platosDisponibles = 3
      logging.info('A comerlaaaaa...')
      semaComensal.release()
      

class Comensal(threading.Thread):
  def __init__(self, numero):
    super().__init__()
    self.name = (f'Comensal {numero}')

  def run(self):
    global platosDisponibles
    global semaCocinero
    global semaComensal
    
    semaComensal.acquire()
    platosDisponibles -= 1
    logging.info(f'¡Qué rico! Quedan {platosDisponibles} platos')
    
    if platosDisponibles == 0:
      logging.info('Cocinero Reponela')
      semaCocinero.release()
    else:
      logging.info('A comerlaaaaa...')
      semaComensal.release()
      

platosDisponibles = 3


Cocinero().start()

for i in range(5):
    Comensal(i).start()

  

