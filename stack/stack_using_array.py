class Stack:

    def __init__(self, max_size):
        self.capacity = max_size
        self.array = [None] * (max_size)
        self.index = -1

    def is_empty(self):
        return self.index == -1

    def size(self):
        return self.index + 1

    def push(self, data):
        self.index += 1
        self.array[self.index] = data

    def pop(self):
        data = self.array[self.index]
        self.index -= 1
        return data

    def peek(self):
        return self.array[self.index]

    def stack_overflow(self):
        return self.index == self.capacity - 1

    def print(self):
        if self.is_empty():
            return
        for i in range(0, self.index + 1):
            print(self.array[i])



if __name__ == '__main__':
    stack = Stack(10)
    print(stack.is_empty())
    stack.push(5)
    print(stack.is_empty())
    print(stack.size())
    stack.push(3)
    stack.push(7)
    stack.push(1)
    stack.print()
    print("Popped element:", stack.pop())
    stack.print()
