#============================Task 1================

def stats(lst:list):
    if not lst: 
        return {
        "min": None,
        "max": None,
        "avg": None,
        "sum": 0
        }
    
    return {
        "min": min(lst),
        "max": max(lst),
        "avg": sum(lst)/len(lst),
        "sum": sum(lst)
    }
# print(stats([10, 20, 30, 40, 50]))

#=====================Task 2=====================

from collections import Counter
import string

def count_words(text):
    clean_text = text.translate(str.maketrans('', '', string.punctuation))
    return dict(Counter(clean_text.lower().split()))

#Task 3


n1 =int(input("first number "))
n2 =int(input("second number "))
operation = input (" what is the operation? write a character ")

if operation == '*':
    sum = n1*n2
    print(sum)
elif operation == '/':
    if n2 == 0:
        print("not allowd!")
    else:
        sum = n1/n2
        print(sum)
elif operation == '+':
    sum = n1+n2
    print(sum)
elif operation == '-':
    sum = n1-n2
    print(sum)
else: print(" try another operation ")

#Task 4

def season(month):
    if month == 12 or 1 or 2:
        print("Winter")
    elif month == 3 or 4 or 5:
        print("Spring")
    elif month == 6 or 7 or 8:
        print("Summer")
    elif month == 9 or 10 or 21:
        print("Autumn")
    else:
        print("Wrong month: ")

# season(2)


#Task 5

def safe_input(prompt,type_func):
    a = 3
    while a > 0:
        data = input(prompt)
        try:
            return type_func(data)
        except(Exception):
            a -= 1
            print("wrong try again")
    print("no more tries left")
    return None


#Task 6

def parse_text(text:str):
    values = text.split(',')
    numbers = []
    errors = []
    for i in values:
        try:
            int(i)
            numbers.append(i)
        except:
            errors.append(i)
    print(numbers, errors)



#Task 7
import random
def generate_password(length, use_digits, use_special):
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    
    chars = letters
    
    if use_digits:
        chars += digits
        
    if use_special:
        chars += special
        
    # Генерируем пароль
    password = ""
    for i in range(length):
        password += random.choice(chars)
        

#Task 8

def apply_to_each(lst, func):
    res = []
    for i in lst:
        res.append(func(i))
    return res



#Task 9
def nested_sum(lst):
    if not lst:
        return 0
    else: 
        return lst[0] + nested_sum(lst[1:])
print(nested_sum([1,2,3,4,5]))

#Task 10

# ?

#Task 11



#Task 12

def count_calls(func):
    calls = 0
    def wrapper(*args, **kwargs):
        nonlocal calls
        calls += 1
        print(calls)
        return func(*args, *kwargs)
    return wrapper

@count_calls
def hello():
    print("hello")


#Task 13



#Task 14



#Task 15



#Task 16


