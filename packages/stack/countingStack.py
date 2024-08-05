from .stack import Stack ;


class CountingStack(Stack):
   def __init__(self):
      Stack.__init__(self)
      self.__counter=0
   
   def get_counter(self):
      return self.__counter
   
   def pop(self):
      self.__counter+=1
      return Stack.pop(self)
