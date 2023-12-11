

class Queue(object):
    def __init__(self):
        self.queue = list()

    def push(self, elem):
        self.queue.append(elem)

    def show(self):
        if self.queue:
            print(self.queue)

    def pop(self):
        index = None
        if self.queue:
            index = self.queue.index(0)
            self.queue.pop(0)
        return index

    def peek(self):
        index = None
        if self.queue:
            index = self.queue.index(0)
        return index

    def empty(self):
        while self.queue:
            print(self.queue.pop(0))


def main():
    stack = Queue()
    for x in range(0, 5):
        print(x)
        stack.push(x)

    stack.show()

    print(stack.pop())
    print(stack.peek())
    #
    # stack.empty()


if __name__ == '__main__':
    main()