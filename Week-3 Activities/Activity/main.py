# Source : https://www.procoding.org/stack-using-array/
class Stack:
    def __init__(self, size=10):
        self._stack = []
        self._size = size

    def push(self, data):
        if len(self._stack) >= self._size:
            raise Exception("Stack overflow")
        else:
            self._stack.append(data)

    def pussing(self):     # Source : https://www.w3schools.com/python/python_lists_loop.asp
        i = 0
        while i <= len(self._stack):

            print(self._stack[::-1])
            self._stack.pop()

    def pop(self):
        if len(self._stack) == 0:
            raise Exception("Stack underflow")
        else:
            return self._stack.pop()

    def chr(self, char):
        if len(self._stack) >= self._size:
            raise Exception("Stack overflow")
        else:
            self._stack.append(char.upper())




stack = Stack()

stack.push(5)
stack.push(6)
stack.push(7)
stack.pussing()



stack.chr("a")
stack.chr("b")
stack.chr("c")
stack.pussing()












