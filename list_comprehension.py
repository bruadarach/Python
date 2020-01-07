##### List Comprehension
cities = [ 'new york city', 'moutain view', 'chigago', 'los angeles']
capitalized_cities = [ city.title() for city in cities ]

print(capitalized_cities)
# ['New York City', 'Moutain View', 'Chigago', 'Los Angeles']


##### If you use 'For Loops'?
cities = [ 'new york city', 'moutain view', 'chigago', 'los angeles']
for city in cities:
    capitalized_cities.append(city.title())
print(capitalized_cities)


##### List Comprehension VS. For Loops
squares = []
for x in range(9):
    squares.append(x**2)
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64]


squares = [x**2 for x in range(9)]
print(squares)
# [0, 1, 4, 9, 16, 25, 36, 49, 64]


##### Placement 
# a = [ EXPRESSION(to be evaluated) / RANGE(iterable)]
squares = [x**2 for x in range(9)]
print(squares)

# b = [ EXPRESSION(to be evaluated) / RANGE(iterable) / IF(condotion) ]
squares = [x**2 for x in range(9) if x % 2 == 0 ]
print(squares)

# c = [ EXPRESSION(to be evaluated) / IF & ELSE (condotionS) / RANGE(iterable) ]

squares = [x**2 for x in range(9) if x % 2 == 0 else x + 3 ]
print(squares)
# ERROR!!!!!!!!!!!!!

squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares)
# [0, 4, 4, 6, 16, 8, 36, 10, 64]