#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 11
    while i > 1:
        i -= 1
        print(i)
        if i == 1:
            print("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    # code goes here!
    int_list = [i * i for i in int_list]
    print(int_list)
    return int_list

list_one = [1,2,3,4,5]
square_integers(list_one)



def fizzbuzz():
    # code goes here!
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
