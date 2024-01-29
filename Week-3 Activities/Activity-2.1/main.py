class Stack:
    def __init__(self, size=13):
        self._stack = []
        self._size = size

    def push(self, data):
        if len(self._stack) >= self._size:
            raise Exception("Stack overflow")
        else:
            self._stack.append(data)

    def pop(self):
        if len(self._stack) == 0:
            raise Exception("Stack underflow")
        else:
            return self._stack.pop()

    def is_empty(self):
        if len(self._stack) == 0:
            print("Stack is empty")

    def is_full(self):
        if len(self._stack) == 13:
            print("Stack is full")

    def get_triangle(self):

        for i in range(1, self._size):
            y = "*"
            self._stack.append(y*(i*2-1))
            print(" " * (self._size-i), "*" * (i*2-1))

        while self._size > 0:

            for i in range(self._size):
                print(" " * i, self._stack[-i], " " * i)
                self._size = self._size - 1






stack = Stack()
stack.get_triangle()
