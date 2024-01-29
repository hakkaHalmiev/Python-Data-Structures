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
          """"
        while 0 > self._size:
            for i in self._stack:
                print(" "*i, self._stack[-i], " "*i)
                self._size = self._size-1
                """



print("hi")






""""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tasarimkodlama.com
stack = []
def yildiz_ucgen_ciz():
    yukseklik = 13
    print("Yıldız üçgen çiziliyor:")
    for i in range(1, yukseklik):
        y = "*"
        stack.append(y*(i*2-1))
        print(" " * (yukseklik - i), "*" * (i * 2 - 1))


yildiz_ucgen_ciz()  # ücgen cizme fonksiyonu çağırılıyor.
# print(stack)
# print(stack[::-1])
print(" "*1, stack[-1], " "*1)
print(" "*2, stack[-2], " "*2)
print(" "*3, stack[-3], " "*3)
"""