# Queues: A linear data structure which has the order of first in first out (FIFO)

class QueueLine:
  def __init__(self):
    self.q = []
   
  def enqueue(self, x):
    self.q.append(x)
  
  def dequeue(self):
    if len(self.q) > 0:
      self.q.pop(0)
  
  def front(self):
    if len(self.q) == 0:
      return None
    return self.q[0]
    
