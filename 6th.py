function def
def calc_sum(a, b): 
    sum = a + b     ## parameter
    print(sum)
    return sum

# calc_sum(5, 12) # function call 

nums = [1,2,3,45,5]
heroes = ["shivam", "saba", "swati"]
def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item, end=" ")

print_list(heroes)
print()


# Factorial #

n = 5

def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        print(fact)

cal_fact(6)

# USD to INR#

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val, "USD =", inr_val, "INR")

converter(83)


# Recursion #

def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)

show(89)


# Practice#
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(10)
print(sum)   

