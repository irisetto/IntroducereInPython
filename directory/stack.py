

class Stack(object):
    def __init__(self):
        self.stack = list()

    def push(self, elem):
        self.stack.insert(0, elem)

    def show(self):
        if self.stack:
            print(self.stack)

    def pop(self):
        index = None
        if self.stack:
            index = self.stack.index(0)
            self.stack.pop(0)
        return index

    def peek(self):
        index = None
        if self.stack:
            index = self.stack.index(0)
        return index

    def empty(self):
        while self.stack:
            print(self.stack.pop(0))


def main():
    stack = Stack()
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