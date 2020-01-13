# [] list comprehension
sq_list = [x**2 for x in range(10)]  # this produces a list of squares
print(sq_list)
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# () iterator
sq_iterator = (x**2 for x in range(10))  # this produces an iterator of squares
print(sq_iterator)
# <generator object <genexpr> at 0x7f8c0ec10308>

print(next(sq_iterator)) # 0
print(next(sq_iterator)) # 1
print(next(sq_iterator)) # 4
print(next(sq_iterator)) # 9
print(next(sq_iterator)) # 16
print(next(sq_iterator)) # 25