#!/usr/bin/env python
# -*- coding: utf-8 -*-


class StackOverflowError(RuntimeError):
    pass


class StackIsEmptyError(RuntimeError):
    pass


class Stack:
    def __init__(self, size):
        self.storage = [0]*size
        self.head = -1
#        self.size = size-1

    def push(self, v):
        if self.head == (len(self.storage)-1):
            raise StackOverflowError()
        else:
            self.head += 1
            self.storage[self.head]=v

    def pop(self):
        if self.head == -1:
            raise StackIsEmptyError()
        else:
            a=self.storage[self.head]
            self.storage[self.head]=0
            self.head -= 1
            return a

    def __len__(self):
        return self.head + 1

#stack1=Stack(5)
#print(stack1.storage)
#stack1.push("{")
#stack1.push("{")
#stack1.push("}")
#stack1.push("{")
#stack1.push("{")
#print(len(stack1),stack1.head)
#stack1.pop()
#stack1.pop()
#stack1.pop()
#stack1.pop()
#print(stack1.pop())
#print(len(stack1),stack1.head)
#print(stack1.storage)
