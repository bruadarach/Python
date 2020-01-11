# yield, yield from, next
"""
yield 키워드를 사용해 generator를 만들어 봅니다.
"""
def test_generagtor():
    yield 1
    yield 2
    yield 3

gen = test_generagtor() # gen는 generator object
print(type(gen)) 
# <class 'generator'>

print(next(gen)) # next()함수를 사용하여, generator object를 인수로 호출한다. 
print(next(gen))
print(next(gen))
print(next(gen))
# 1
# 2
# 3
# StopIteration

"""
yield 키워드를 사용해 generator를 만들어 봅니다.
"""
def test_generator2(maxnum):
    for i in range(maxnum):
        yield i

gen2 = test_generator2(5)
print(next(gen2)) # 0
print(next(gen2)) # 1
print(next(gen2)) # 2
print(next(gen2)) # 3
print(next(gen2)) # 4
print(next(gen2)) # StopIteration 

"""
이렇게 생성한 genertaor는 iterable한 객체가 되며 for문에서 사용할 수 있습니다.
"""
for i in test_generator(3):
    print(i)

# 1
# 2
# 3

"""
이렇게 생성한 genertaor는 iterable한 객체가 되며 for문에서 사용할 수 있습니다.
"""
for i in test_generator2(5):
    print(i)
    
# 0
# 1
# 2
# 3
# 4

"""
generator를 동시에 두개 생성하면, 서로가 다른 객체이며, 각기 따로 동작합니다.
"""
def test_generator():
    yield 1
    yield 2
    yield 3

h = test_generator()
i = test_generator()

print(h == i) # false 
print(h is i) # false

print(next(h)) # 1
print(next(h)) # 2
print(next(i)) # 1
print(next(h)) # 3
print(next(i)) # 2
print(next(i)) # 3

"""
제너레이터 식: 우리가 알고 있는 리스트, Set, Dictionary의 표현식의 내부도 사실 generator입니다.
"""
def test_generator2(maxnum):
    for i in range(maxnum):
        yield i

for i in test_generator2(5):
    print(i)
# 0
# 1
# 2
# 3
# 4

##### 제너레이터 식: 위 제너레이터의 정의와 초기화는 내포 표현을 사용하여 아래와 같이 간결하게 기술할 수 있다.

g = (x for x in range(5))
print(g)
# <generator object <genexpr> at 0x7ff0a8b5d308>
print(type(g))
# <class 'generator'>

t = [x for x in range(5)]
print(t) # [0, 1, 2, 3, 4] 
# list
print(type(t))
# list

"""
yield from : yield문은 한번씩 값을 바깥으로 전달했습니다. 여러번 바깥으로 전달할려면 for문을 아래와 같이 사용해야합니다.
"""
def three_generator():
    a = [1, 2, 3]
    for i in a:
        yield i

gen = three_generator()
print(list(gen)) # [1, 2, 3]
print(list(gen)) # []
print(list(gen)) # []

"""
using "yield from" : 
yield문은 한번씩 값을 바깥으로 전달했습니다. 
여러번 바깥으로 전달할려면 for문 대신 아래와 같이 사용해야합니다.
즉, for문 대신에 iterable한객체를 yield할 때는 yield from iterable 로 값을 전달할 수 있습니다.
"""
def three_generator():
    a = [1, 2, 3]
    yield from a # instead of "for loops" below
    # for i in a:
    #     yield i
    
gen = three_generator()
print(list(gen))
print(list(gen))
print(list(gen))

# [1, 2, 3]
# []
# []

""" yield"""
def number_generator():
    x = [1, 2, 3]
    for i in x:
        yield i
 
for i in number_generator():
    print(i)
# 1
# 2
# 3

""" yield from : 이런 경우에는 매번 반복문을 사용하지 않고, yield from을 사용하면 됩니다."""
def number_generator():
    x = [1, 2, 3]
    yield from x    # 리스트에 들어있는 요소를 한 개씩 바깥으로 전달
 
for i in number_generator():
    print(i)
# 1
# 2
# 3

"""
yield from x와 같이 yield from에 리스트(반복 가능한 객체)를 지정했습니다. 
이렇게 하면 리스트에 들어있는 요소를 한 개씩 바깥으로 전달합니다. 
즉, yield from을 한 번 사용하여 값을 세 번 바깥으로 전달합니다. 
따라서 next 함수(__next__ 메서드)를 세 번 호출할 수 있습니다.
"""
def number_generator():
    x = [1, 2, 3]
    yield from x
    
g = number_generator()

print(next(g)) # 1 
print(next(g)) # 2
print(next(g)) # 3
print(next(g)) # StopIteration:

"""
yield from에 제너레이터 객체 지정
"""
def number_generator(stop):
    n = 0
    while n < stop:
        yield n
        n += 1
 
def three_generator():
    yield from number_generator(3)    # 숫자를 세 번 바깥으로 전달
 
for i in three_generator():
    print(i)
# 0
# 1
# 2

"""
먼저 제너레이터 number_generator는 매개변수로 받은 숫자 직전까지 숫자를 만들어냅니다. 
그리고 three_generator에서는 yield from number_generator(3)과 같이 yield from에 제너레이터 객체를 지정했습니다.
number_generator(3)은 숫자를 세 개를 만들어내므로 yield from number_generator(3)은 숫자를 세 번 바깥으로 전달합니다. 
따라서 for 반복문에 three_generator()를 사용하면 숫자를 세 번 출력합니다
(next 함수 또는 __next__ 메서드도 세 번 호출 가능).
"""

