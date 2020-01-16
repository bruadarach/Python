# Step 1
def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

"""
print("Testing mean function")
n_list = [34, 44, 23, 46, 12, 24]
correct_mean = 30.5
assert(mean(n_list) == correct_mean)

print("Testing add_five function")
correct_list = [39, 49, 28, 51, 17, 29]
assert(add_five(n_list) == correct_list)

print("All tests passed!")
"""
# Testing mean function
# Testing add_five function
# All tests passed!


"""
가정 설정문(assert)
: assert는 뒤의 조건이 True가 아니면 AssertError를 발생한다.

a = 3
assert a == 2

#결과
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError

왜 assert가 필요한 것일까?

어떤 함수는 성능을 높이기 위해 반드시 정수만을 입력받아 처리하도록 만들 수 있다. 이런 함수를 만들기 위해서는 반드시 함수에 정수만 들어오는지 확인할 필요가 있다. 이를 위해 if문을 사용할 수도 있고 '예외 처리'를 사용할 수도 있지만 '가정 설정문'을 사용하는 방법도 있다.

아래 코드는 함수 인자가 정수인지 확인하는 코드이다.

lists = [1, 3, 6, 3, 8, 7, 13, 23, 13, 2, 3.14, 2, 3, 7]

def test(t):
    assert type(t) is int, '정수 아닌 값이 있네'

for i in lists:
    test(i)
#결과
AssertionError: 정수 아닌 값이 있네

lists에 실수가 하나 있으므로 AssertionError가 발생했다. assert 문은 다음 형식으로 작동한다.

assert 조건, '메시지'

'메시지'는 생략할 수 있다.

assert는 개발자가 프로그램을 만드는 과정에 관여한다. 원하는 조건의 변수 값을 보증받을 때까지 assert로 테스트 할 수 있다.

이는 단순히 에러를 찾는것이 아니라 값을 보증하기 위해 사용된다.

예를 들어 함수의 입력 값이 어떤 조건의 참임을 보증하기 위해 사용할 수 있고 함수의 반환 값이 어떤 조건에 만족하도록 만들 수 있다. 혹은 변수 값이 변하는 과정에서 특정 부분은 반드시 어떤 영역에 속하는 것을 보증하기 위해 가정 설정문을 통해 확인 할 수도 있다.

이처럼 실수를 가정해 값을 보증하는 방식으로 코딩 하기 때문에 이를 '방어적 프로그래밍'이라 부른다.
"""

### Step 2
### By including these excutable statements inside this main block,
### we tell Python to execute this code only when the main program being executed is this name_main_ex.py
### if we run this file the code inside this block(= if__name__ 안에 들은 내용들) is run

### however, if ths file is imported to another file, the code of if __name__ part is not run! 

### What is name & main?
### => whenever we run a script like this, Python actually sets a special built-in variable 
### => the built-in variable called 'Name' with two underscores before and after it for any module.

### since we run Python import_local_script.py, Python recognize this module 'import_local_script.py' as the main program
### and, sets the name variable for this module to the string Main.

### for any modules that are imported in the script, 
### this built-in name variable is just set to the name of that module
def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]
"""
if __name__ == '__main__':
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")
"""
# Testing mean function
# Testing add_five function
# All tests passed!


### Other version to use def main(): and if?
def mean(num_list):
    return sum(num_list) / len(num_list)

def add_five(num_list):
    return [n + 5 for n in num_list]

def main():
    print("Testing mean function")
    n_list = [34, 44, 23, 46, 12, 24]
    correct_mean = 30.5
    assert(mean(n_list) == correct_mean)

    print("Testing add_five function")
    correct_list = [39, 49, 28, 51, 17, 29]
    assert(add_five(n_list) == correct_list)

    print("All tests passed!")

#Therefore, the condition if __name__ == "__main__"is just checking whether this module is the main program.
if __name__ == '__main__':
    main()
# Testing mean function
# Testing add_five function
# All tests passed!