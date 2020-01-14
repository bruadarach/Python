x = int(input("Enter a number: "))
# When you type "nope", an error occurs below
# ValueError: invalid literal for int() with base 10: 'nope'

##### How to handle with a 'try' statement?
try:
    x = int(input('Enter a number: '))
except:
    print('That\'s not a valid number!')

# Enter a number: nope
# That's not a valid number!


##### How to handle with a 'try' statement?
##### 1. the try statement is executed well and the last print statement is not printed.
try:
    x = int(input('Enter a number: '))
except:
    print('That\'s not a valid number!')

print('\nAttempted Input\n')
# Enter a number: 10


##### 2. the try statement is not executed, but the except and last print statement are printed.
try:
    x = int(input('Enter a number: '))
except:
    print('That\'s not a valid number!')

print('\nAttempted Input\n')
# Enter a number: ten
# That's not a valid number!

# Attempted Input


##### If we want this code to keep running until the user inputs a valid number
##### Use a 'while loop' and 'break the loop' if all the code in the try block successfully executes.
### while + break! 
while True:
    try:
        x = int(input('Enter a number: '))
        break # never print the 'Attenpted Input'!
    except:
        print('That\'s not a valid number!')
    
    print('\nAttempted Input\n')

# Enter a number: ten
# That's not a valid number!

# Attempted Input

# Enter a number: two
# That's not a valid number!

# Attempted Input

# Enter a number: 10


##### If we want to this list line to always run after the try statement no matter what,
##### There is an optional component of the statement we can use.
##### 'Finally' : Before Python leaves this try statement, it will run the code in this finally block under any conditions
try:
    x = int(input('Enter a number: '))
except:
    print('That\'s not a valid number!')
finally:
    print('\nALWAYS PRINT: Attempted Input\n')

# Enter a number: 10

# ALWAYS PRINT: Attempted Input


try:
    x = int(input('Enter a number: '))
except:
    print('That\'s not a valid number!')
finally:
    print('\nALWAYS PRINT: Attempted Input\n')
    
# Enter a number: ten
# That's not a valid number!

# ALWAYS PRINT: Attempted Input



##### while loop + try + except + finally
while True:
    try:
        x = int(input('Enter a number: '))
        break # never print the 'Attenpted Input'!
    except:
        print('That\'s not a valid number!')
    
    finally:
        print('\nAttempted Input\n')

# Enter a number: ten
# That's not a valid number!

# Attempted Input

# Enter a number: wow
# That's not a valid number!

# Attempted Input

# Enter a number: 10

# Attempted Input


##### Specifying Exceptions
# 특정한 에러(ValueError)가 아닌 다른 에러(KeyboardInterrupt) 발생시에는 execute 되지 않고 프로그램이 바로 멈춘 뒤 에러가 뜸!
# because,  KeyboardInterrupt is not handled by the try/except statement! 
# Still, teh finally block was still executed!  
while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError: # A specific error set up
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')

# Enter a number: ^C
# Attempted Input

# Traceback (most recent call last):
#   File "practice.py", line 2, in <module>
#     x = int(input('Enter a number: '))
# KeyboardInterrupt


##### If we want this handler to address more than one type of exception?
##### add another except as a tuple!
while True: 
    try:
        x = int(input('Enter a number: '))
        break
    except (ValueError, KeyboardInterrupt):
        print('That\'s not a valid number!')
    finally:
        print('\nAttempted Input\n')

    
##### If we want to execute different blocks of code, depending on the exception, 
##### multile except blocks! 
while True:
    try:
        x = int(input('Enter a number: '))
        break
    except ValueError:
        print('That\'s not a valid number!')
    except KeyboardInterrupt:
        print('\nNo input taken')
        break # break from the while loop
    finally:
        print('\nAttempted Input\n')

# Enter a number: hahaha
# That's not a valid number!

# Attempted Input


# Enter a number: ^C
# No input taken

# Attempted Input


##### e.g) handling_errors
def party_planner(cookies, people):
    leftovers = None
    num_each = None
    # TODO: Add a try-except block here to
    #       make sure no ZeroDivisionError occurs.
    try:
        num_each = cookies // people
        leftovers = cookies % people
    
    except ZeroDivisionError:
    print("Oops, you entered 0 people will be attending.")
    print("Please enter a good number of people for a party.")

    return(num_each, leftovers)

# The main code block is below; do not edit this
lets_party = 'y'
while lets_party == 'y':

    cookies = int(input("How many cookies are you baking? "))
    people = int(input("How many people are attending? "))

    cookies_each, leftovers = party_planner(cookies, people)

    if cookies_each:  # if cookies_each is not None
        message = "\nLet's party! We'll have {} people attending, they'll each get to eat {} cookies, and we'll have {} left over."
        print(message.format(people, cookies_each, leftovers))

    lets_party = input("\nWould you like to party more? (y or n) ")

# How many cookies are you baking? 30
# How many people are attending? 5

# Let's party! We'll have 5 people attending, they'll each get to eat 6 cookies, and we'll have 0 left over.

# Would you like to party more? (y or n) y
# How many cookies are you baking? 22
# How many people are attending? 5

# Let's party! We'll have 5 people attending, they'll each get to eat 4 cookies, and we'll have 2 left over.

# How many cookies are you baking? 10
# How many people are attending? 0
# Oops, you entered 0 people will be attending
# Please enter a good number of people for a party.

# Would you like to party more? (y or n) n


##### Accessing Error Messages
### When you handle an exception, you can still access its error message like this:
try:
    x = int(input('Enter a number: '))
    y = 10 / x
    print(y)
except ZeroDivisionError as e: # # e에 저장된 에러 메시지 출력 # 보통 예외( exception)의 e를 따서 변수 이름을 e로 짓습니다.
    print("ZeroDivisionError occurred: {}".format(e))

# Enter a number: 10
# 1.0

# Enter a number: 0
# ZeroDivisionError occurred: division by zero


### If you don't have a specific error you're handling, you can still access the message like this:
try:
    x = int(input('Enter a number: '))
    y = 10 / x
    print(y)
except Exception as e:
   print("Exception occurred: {}".format(e))

# Enter a number: 0
# Exception occurred: division by zero

# Enter a number: ten
# Exception occurred: invalid literal for int() with base 10: 'ten'

# I think, try-else statement, Not working in a while loop
# 예외처리에 else 를 사용하여 아무 에러도 발생하지 않았을 경우 실행할 명령을 지정해줄 수 있다.
# else 는 예외가 발생하면 실행되지 않는다.

# while True: 
try:
    x = int(input('Enter a number: '))
    #break
except:
    print('That\'s not a valid number!')
else:
    print("try is sucessful!")
finally: # else 문과는 달리 에러가 발생해도 실행되는 것을 볼 수 있다.
    print('\nALWAYS PRINT: Attempted Input\n')

# Enter a number: ten
# That's not a valid number!

# ALWAYS PRINT: Attempted Input

# =================================
# Enter a number: 10
# try is sucessful!

# ALWAYS PRINT: Attempted Input


##### C.f) raise 에러 발생시키기
# raise 문을 사용하면 일부러 에러를 발생시킬 수 있다.
# 다음은 my_list 내의 요소들을 하나씩 돌면서 출력해주는 for 문이다. 
# 리스트 내의 요소가 3 일 경우 ZeroDivisionError 가 나도록 해보았다.
my_list = [1, 2, 3, 4, 5]

for i in my_list:
    print(i)
    if i == 3:
        raise ZeroDivisionError

# 1
# 2
# 3
# Traceback (most recent call last):
#   File "practice.py", line 6, in <module>
#     raise ZeroDivisionError
# ZeroDivisionError

# 실제로 어떤 수를 0으로 나눈 적이 없지만 ZeroDivisionError 가 발생한 것을 볼 수 있다.
# 이렇게 일부러 에러를 발생시키고 예외처리하여 특정 상황에 대해 실행할 명령을 사용자의 입맛에 맞게 구성할 수 있다.