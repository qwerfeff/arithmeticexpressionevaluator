class Stack:
   def __init__(self):
       self.items=[]
   def push(self,item):
       self.items.append(item)
   def pop(self):
       if self.is_empty():
           raise IndexError("Cannot pop items from an empty stack")
       return self.items.pop()
   def peek(self):
       if self.is_empty():
           raise IndexError("Peek from an empty stack")
       return self.items[-1]
   def is_empty(self):
       return len(self.items) == 0
   def size(self):
       return len(self.items)
class Queue:
    def __init__(self):
        self.items = {}
        self.front_index = 0
        self.rear_index = 0
    def enqueue(self, item):
        self.items[self.rear_index] = item
        self.rear_index += 1
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        item = self.items[self.front_index]
        del self.items[self.front_index]
        self.front_index += 1
        return item
    def front(self):
        if self.is_empty():
            raise IndexError("Cannot access front of an empty queue")
        return self.items[self.front_index]
    def rear(self):
        if self.is_empty():
            raise IndexError("Cannot access rear of an empty queue")
        return self.items[self.rear_index - 1]
    def is_empty(self):
        return self.front_index == self.rear_index
    def size(self):
        return self.rear_index - self.front_index
class ArithmeticExpression:
   def __init__(self,string):
       self.string=string
   def number_of_instances_of_operator(self, operator):
       if operator in ["+","~","*","/","^","(",")"]:
           return self.string.count(operator)
       else:
           raise SyntaxError("Only operators +,~,*,/,^,(,) are valid for parameter ==> operator")
   def location_of_instance(self,instance,operator):
       if operator in ["+", "~", "*", "/", "^","(",")"] and type(instance) is int:
           n=0
           if instance == 1:
               return self.string.find(operator)
           if instance == -1:
               return self.string.rfind(operator)
           else:
               for i in range(len(self.string)):
                   if self.string[i] == operator:
                       n = n + 1
                   if n == instance:
                       return i
       if instance > self.number_of_instances_of_operator(operator):
           raise IndexError("Instance given is more than total number of instances of operator")
       if instance < -1:
           raise IndexError("Only positive integers and -1 valid for parameter ==> instance")
       if operator not in ["+", "~", "*", "/", "^","(",")"] and not type(instance) is int:
           raise SyntaxError("Only operators +,~,*,/,^,(,)  are valid for parameter ==> operator,Incorrect data type only positive integers and -1 valid for parameter ==> instance")
       if operator not in ["+", "~", "*", "/", "^","(",")"]:
           raise SyntaxError("Only operators +,~,*,/,^,(,) are valid for parameter ==> operator")
       if not type(instance) is int:
           raise SyntaxError("Incorrect data type only positive integers and -1 valid for parameter ==> instance")
