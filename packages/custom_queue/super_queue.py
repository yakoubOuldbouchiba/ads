from .queue import Queue
class SuperQueue(Queue):
    def __init__(self):
        super().__init__()
    
    def isempty(self):
        return len(self._Queue__queue_list) == 0
