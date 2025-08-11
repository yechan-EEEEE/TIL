# push
stack = []
def push(item):
    stack.append(item)

class Stack:
    def __init__(self,capacity=10):
        self.capacity = capacity #초기 용량을 설정
        self.items = [None] * capacity
        self.top = -1
    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise IndexError("Stack is full")
        self.top += 1
        self.items[self.top] = item
# pop
stack = []
def pop():
    if len(stack) == 0:
        print("데이터가 없습니다.")
        return
    return stack.pop()

class Stack:
    def is_empty(self):
        return self.top == -1
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        item = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1
        return item
    def is_empty(self):
        return self.top == -1
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[self.top]
