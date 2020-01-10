"""
filter() is a higher-order built-in function that takes a function and iterable as inputs and returns an iterator with the elements from the iterable for which the function returns True.
"""

# 1. basic
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6])) # [1,2,6]


# 2. filter with a function
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))


# 3. filter + lambda
list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
# [1, 2, 6]


# 4. the other example
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)

# Answer
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

short_cities = list(filter(lambda x: len(x) < 10, cities))
print(short_cities)


