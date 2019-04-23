#!/usr/bin/env python
# -*- coding: utf-8 -*-
from stack import Stack, StackOverflowError, StackIsEmptyError
#Мне кажется, что это можно и более кратко задать, но я предполагаю, что так быстрее функция будет работать
def is_paranthesis_balanced(s):
#    dic={"[":"]","{":"}","<":">","(":")"}
    sko="{[<("
    skc="}]>)"
    dic={sko[a]: skc[a] for a in range(len(sko))}
    if len(s)%2 != 0 or len(s)==0:
        return False
    else:
        stack1=Stack(int(len(s)/2))
    for char in s:
        if char in sko:
            stack1.push(char)
        elif char in skc:
            if len(stack1) == 0:
                return False
            else:
                x=stack1.pop()  #Кажется, можно обойтись и без доп.переменной x
                if char != dic.get(x):
                    return False
                else:
                    continue
    if len(stack1)==0: #На самом деле, это уже избыточное условие
        return True
    return False