#!/usr/bin/env


def max_number(num1, num2, num3):
    answer = 0
    if num1 > num2 and num1 > num3:
        answer = num1
    elif num2 > num1 and num2 > num3:
        answer = num2
    else:
        answer = num3
    print(f"The max number is {answer}")


def sum_numbers(nums):
    the_sum = 0
    for num in nums:
        the_sum += num
    print(f"The sum of the list is {the_sum}")


def multiply_numbers(nums):
    product = 1
    for num in nums:
        product *= num
    print(f"The product of the list is {product}")


def upper_and_lower(phrase):
    upper_count = 0
    lower_count = 0
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    for char in phrase:
        if char in upper:
            upper_count += 1
        elif char in lower:
            lower_count += 1

    print(f"There are {upper_count} upper-case letters and {lower_count} lower-case letters")


