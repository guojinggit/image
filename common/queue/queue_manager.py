try:
    import Queue           # python2
except ImportError:
    import queue as Queue  # python3

class Queue_manager():

    my_queue = []

    def __init__(self, queue_num, queue_size):
        for i in queue_num:
            self.my_queue[i] = Queue.Queue(queue_size)

    def get_queue(self, index = 0):
        return self.my_queue[0] if index > len(self.my_queue) -1 else self.my_queue[index]

    def push(self, data_class, index=0):
        if index > len(self.my_queue) - 1:
            self.my_queue[0].put(data_class)
        else:
            self.my_queue[index].put(data_class)

    def pop(self, index=0):
        if index > len(self.my_queue) - 1:
            self.my_queue[0].get()
        else:
            self.my_queue[index].get()

