''' Step 1. How to import from a script file

    # How to import a module? import mymodule.py into myprogram.py
    # Which files you need?

        - 1. myprogram.py
            - from mymodule import my_func
                my_func()

        - 2. mymodule.py
            def my_func():
                print("Hey I am in mymodule.py")
'''

"""
from mymodule import my_func

my_func()
"""


''' Step 1 Running Result'''
# datasciencestudy@SUui-MacBookPro python_review % python3 myprogram.py 
# Hey I am in mymodule.py




''' Step 2 : How to import from a folder

    # Mudole Directories

        ㄴmyprogram.py (*MAIN FILE TO RUN)
        ㄴMaMainPackage
            ㄴ__init__.py : tell Python that hey, it's actual directory, and it has a bunch of modules.py in it, so you can call them, using a certain context we will show you 
            ㄴ some_main_script.py
            ㄴ (...many main script.py files in the main package folder)
            ㄴ__pychache__ : after running the package(especially __init__.py), this directory will be created
                ㄴ__init__.cpython-37.pyc
                ㄴsome_main_script.cpython-37.pyc

            ㄴ SubPackage
                ㄴ__init__.py
                ㄴmysubscript.py
                ㄴ__pychache__ : after running the package(especially __init__.py), this directory will be created
                    ㄴ__init__.cpython-37.pyc
                    ㄴmysubscript.cpython-37.pyc
'''
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

some_main_script.main_report() # def main_report() IN some_main_script.py IN MyMainPackage(folder)

mysubscript.sub_report() # def sub_report() IN mysubscript.py IN Subpackage(folder) IN MyMainPackage(folder)

''' Step 2 Running Result '''
# datasciencestudy@SUui-MacBookPro python_review % python3 myprogram.py 
# Hey I am in some_main_script.py in MainPackage
# Hey I am a function inside mysubscript.py in SubPackage


""" Additional Comment : After running the package, you will see a '__pycache__' folder created with __init__.cpython-37.pyc, some_main_script.cpython-37.pyc files.
6.1.3. 《컴파일된》 파이썬 파일
모듈 로딩을 빠르게 하려고, 파이썬은 __pycache__ 디렉터리에 각 모듈의 컴파일된 버전을 module.version.pyc 라는 이름으로 캐싱합니다. 
version 은 컴파일된 파일의 형식을 지정합니다; 일반적으로 파이썬의 버전 번호를 포함합니다. 
예를 들어, CPython 배포 3.3 에서 spam.py 의 컴파일된 버전은 __pycache__/spam.cpython-33.pyc 로 캐싱 됩니다. 
이 명명법은 서로 다른 파이썬 배포와 버전의 컴파일된 모듈들이 공존할 수 있도록 합니다.

파이썬은 소스의 수정 시간을 컴파일된 버전과 비교해서 시효가 지나 다시 컴파일해야 하는지 검사합니다. 
이것은 완전히 자동화된 과정입니다. 또한, 컴파일된 모듈은 플랫폼 독립적이기 때문에, 같은 라이브러리를 서로 다른 아키텍처를 갖는 시스템들에서 공유할 수 있습니다.
"""
