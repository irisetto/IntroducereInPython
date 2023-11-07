
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1]

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack)
    print("Pop:", stack.pop())  
    print("Peek:", stack.peek())  
    print(stack.stack)
    print("Pop:", stack.pop())  
    print("Pop:", stack.pop())  
    print("Pop:", stack.pop())  
    print(stack.stack)

if __name__ == "__main__":
    main()