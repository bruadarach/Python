"""
map() is a higher-order built-in function that takes a function and iterable as inputs, and returns an iterator that applies the function to each element of the iterable. 
"""

# 1. basic
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)


# 2. map3
def two_times(x): 
    return x*2

list(map(two_times, [1, 2, 3, 4]))
[2, 4, 6, 8]


# 3. map + lambda
list(map(lambda a: a*2, [1, 2, 3, 4]))
[2, 4, 6, 8]


# 4. the other example
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

def mean(num_list):
    return sum(num_list) / len(num_list)

averages = list(map(mean, numbers))
print(averages)

# Answer
numbers = [
              [34, 63, 88, 71, 29],
              [90, 78, 51, 27, 45],
              [63, 37, 85, 46, 22],
              [51, 22, 34, 11, 18]
           ]

averages = list(map(lambda x: sum(x) / len(x), numbers))
print(averages)