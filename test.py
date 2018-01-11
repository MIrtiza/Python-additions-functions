import logging

def add(x,y):
    return x+y


def sub(x,y):
    return x-y

def mul(x,y):

    return x*y

def div(x,y):
    return x/y

num1 = 4
num2 =10

add_result = add(num1,num2)
print('Add: {} + {} = {}'.format(num1,num2,add_result))

add_result = sub(num1,num2)
print('sub: {} - {} = {}'.format(num1,num2,add_result))

add_result = mul(num1,num2)
print('multiple: {} x {} = {}'.format(num1,num2,add_result))

add_result = div(num1,num2)
print('divide {} / {} = {} '.format(num1,num2,add_result))