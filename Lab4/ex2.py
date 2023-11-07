
class Queue:
    def __init__(self):
        self.queue = []

    def push(self, item):
        self.queue.append(item)

    def pop(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)

    def peek(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue[0]

def main():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.queue)
    print("Pop:", queue.pop())  
    print("Pop:", queue.pop())  
    print(queue.queue)
    print("Pop:", queue.pop())  
    print("Pop:", queue.pop())

if __name__ == "__main__":
    main()