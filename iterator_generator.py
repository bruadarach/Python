lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):
    count = start
    for element in iterable:
        yield count, element
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))

# Lesson 1: Why Python Programming
# Lesson 2: Data Types and Operators
# Lesson 3: Control Flow
# Lesson 4: Functions
# Lesson 5: Scripting


def chunker(iterable, size):
    """Yield successive chunks from iterable of length size."""
    for i in range(0, len(iterable), size):
        yield iterable[i:i + size]

for chunk in chunker(range(25), 4):
    print(list(chunk))
    
# [0, 1, 2, 3]
# [4, 5, 6, 7]
# [8, 9, 10, 11]
# [12, 13, 14, 15]
# [16, 17, 18, 19]
# [20, 21, 22, 23]
# [24]


# Additional Explanation
print(range(25)) # range(0, 25)

for i in range(0, len(range(25)), 4):
    print(i)
# 0
# 4
# 8
# 12
# 16
# 20
# 24

print(range(25)[0:4]) # range(0, 4)
print(list(range(0,4))) # [0, 1, 2, 3]