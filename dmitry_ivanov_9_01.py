###############################################
### FIFO queue implementation using classes ###
###############################################

# custom exception fot Queue.get() error
class QueueError(IndexError):
    def __str__(self):
        return "The queue is empty"

# main queue class
class Queue:
    def __init__(self):
        self.__q = []

    def put(self, elem):
        self.__q.append(elem)

    def get(self):
        if len(self.__q) == 0:
            raise QueueError
        else:
            first = self.__q[0]
            new_q = []
            for i in range(1, len(self.__q)):
                new_q.append(self.__q[i])
            self.__q = new_q.copy()
            return first

que = Queue()

que.put(1)
que.put('dog')
que.put(False)

try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
