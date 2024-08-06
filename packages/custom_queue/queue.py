from .queue_error import  QueueError
class Queue:
    def __init__(self):
        self.__queue_list=[]

    def put(self, elem):
        self.__queue_list.append(elem)

    def get(self):
        if (len(self.__queue_list)==0):
            raise QueueError();
        val =  self.__queue_list[0]
        del self.__queue_list[0]
        return val