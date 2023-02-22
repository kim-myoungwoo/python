#!/usr/bin/env python
# coding: utf-8

# In[2]:


# test_module.py 생성
PI = 3.14

def number_input():
    output = input('숫자 입력 > ')
    return float(output)

def get_circumference(radius):
    return PI * 2 * radius

def get_circle_are(radius):
    return PI * radius * radius

print('test program name ->', __name__)

