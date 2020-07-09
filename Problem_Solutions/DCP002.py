""" QUESTION
    Basic Info :This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Challenge : what if you can't use division?

SOLUTION"""
# This is the initial solution. Challenge is not Considered in this. This makes the problem easier
#   Solution 1
# import functools as ft
# def arrayProductExcept(arr):  # Don't worry this is my personal naming way, nothing to get scared. It's called camelCasing btw.
#     l = lambda x,y:x*y
#     product = ft.reduce(l,arr)
#     print(*[product//i for i in arr])


# arr = [1, 2, 3, 4, 5]
# arrayProductExcept(arr)


# Now we shall consider the challenge. There are two ways to perform divisions without using '/' operator (or performing division as division)
# First we subtract the divisor form dividend until divisor is less than dividend. The number of times we perform subtraction is the quotient
# Second we use Bit Manipulation (Welcome To PowerFul Programming)
# Here are some links about using Bit Manipulation for division
# 1. GeeksForGeeks : https://www.geeksforgeeks.org/divide-two-integers-without-using-multiplication-division-mod-operator/
# 2. StackverFlow : https://stackoverflow.com/questions/5284898/implement-division-with-bit-wise-operator
# By the way if you are new to programming and this is your first repo you are visiting, you better make a note of these two sites.




import functools as ft

def divide(dividend, divisor):
    # We first calculate the sign of divisor (-ve or +ve). sign will be -ve only if  either one them is negative else it is positive
    sign = (-1 if((dividend < 0) ^ (divisor < 0)) else 1)
    # remove sign of operands
    dividend = abs(dividend)
    divisor = abs(divisor)
    # Initialize the quotient
    quotient = 0
    temp = 0
    # test down from the highest bit and accumulate the tentative value for valid bit
    for i in range(31, -1, -1):
        if (temp + (divisor << i) <= dividend):
            temp += divisor << i
            quotient |= 1 << i
    return sign * quotient

def arrayProductExcept(arr):  # Don't worry this is my personal naming way, nothing to get scared. It's called camelCasing btw.
    l = lambda x,y:x*y
    product = ft.reduce(l,arr)
    print(*[divide(product,i) for i in arr])

arr = [1, 2, 3, 4, 5]
arrayProductExcept(arr)