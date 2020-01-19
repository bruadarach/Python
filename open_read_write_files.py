##### interact with real-world data

f = open('/Users/datasciencestudy/Desktop/python_review/some_file.txt', 'r') # open : open a file # r = only reading 
file_data = f.read() # read : access the contents of this file and put it into a string!  
# we assign the string returned from this method into the variable 'file_data'

# when we finished with the file f, we should close it! 
# this will free up any system resources taken up by the file. 
# it is important to always close files we have opened once we no longer need them.
f.close()

print(file_data)
# Hello!!

# You've read the contents of this file!


##### Adding numbers in a file?
files = []
for i in range(10): 
    # if it is range(10000), the system no longer ahd available resource to open a new files!
    # Traceback (most recent call last):
    # File "reading_writing_files.py", line 21, in <module>
    # OSError: [Errno 23] Too many open files in system: 'some_file.txt'
    files.append(open('some_file.txt', 'r'))
    print(i)
# Hello!!

# You've read the contents of this file!
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9


### if it is range(10000), the system no longer and available resource to open a new files!
files = []
for i in range(10): 
    files.append(open('some_file.txt', 'r'))
    print(i)
# 7826
# 7827
# 7828
# Traceback (most recent call last):
# File "reading_writing_files.py", line 21, in <module>
# OSError: [Errno 23] Too many open files in system: 'some_file.txt'
    

##### WRITING MODE!
##### f = open('file.txt', 'w') 
### Be careful, once you open a file in writing mode, 
### Anythin that it contained previously will be deleted!!
 

##### If you are interested in adding to an existing file without deleting its content, 
##### you should use append instead of write! 
f = open('some_file.txt','a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

# Hello!!

# You've read the contents of this file!11번째 줄입니다.
# 12번째 줄입니다.
# 13번째 줄입니다.
# 14번째 줄입니다.
# 15번째 줄입니다.
# 16번째 줄입니다.
# 17번째 줄입니다.
# 18번째 줄입니다.
# 19번째 줄입니다.


##### If the file does not exist, Python will create for you!
f = open('another_file.txt', 'w')
f.write('Hello World!')
f.close()


##### 'with'
##### Automatically close()
##### auto-closes a file for you once you're finished using it.
with open('another_file.txt', 'r') as f:
    file_data = f.read()
# we don't have to add 'f.close()'

# This with keyword allows you to open a file, do operations on it, and automatically close it after the indented code is executed, in this case, reading from the file. Now, we don’t have to call f.close()! You can only access the file object, f, within this indented block.

### e.g) using open(), f.close()
f = open("basic_close.txt", 'w')
f.write("Life is too short, you need python")
f.close()

### e.g) using 'with' open

# 파일을 열면 위와 같이 항상 close해 주는 것이 좋다. 
# 하지만 이렇게 파일을 열고 닫는 것을 자동으로 처리할 수 있다면 편리하지 않을까? 
# 파이썬의 with문이 바로 이런 역할을 해준다. 
# 다음 예는 with문을 사용해서 위 예제를 다시 작성한 모습이다.
with open("with_open_close.txt", "w") as f:
    f.write("Life is too short, you need python")

##### read(number)
# If you pass the read method an integer argument, 
# it will read up to that number of characters, output all of them, and 
# keep the 'window' at that position ready to read on.

# camelot.txt 
'''
We're the knights of the round table
We dance whenever we're able
'''
with open("camelot.txt") as song:
    print(song.read(2)) # number of characters! 
    print(song.read(8))
    print(song.read())
# We
# 're the 
# knights of the round table
# We dance whenever we're able


##### readlines()
# f.readline() reads a single line from the file; 
# a newline character (\n) is left at the end of the string, 
# and is only omitted on the last line of the file 
# if the file doesn’t end in a newline.

with open("/Users/datasciencestudy/Desktop/python_review/camelot.txt") as song:
    print(song.readline())
    print(song.readline())
    print("finished!")
# We're the knights of the round table

# We dance whenever we're able
# finished!


with open("/Users/datasciencestudy/Desktop/python_review/camelot.txt") as song:
    print(song.readlines())
# ["We're the knights of the round table\n", "We dance whenever we're able"]


##### strip()
# Conveniently, Python will loop over the lines of a file using the syntax for line in file. 
# I can use this to create a list of lines in the file. 
# Because each line still has its newline character attached, 
# I remove this using .strip().
 
camelot_lines = []
with open("/Users/datasciencestudy/Desktop/python_review/camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)
# ["We're the knights of the round table", "We dance whenever we're able"]


##### C.f) strip? remove whitespace
# lstrip() : remove the left whitespace
a = " hi "
a.lstrip()
# 'hi '


# rstrip() : remove the right whitespace
a = " hi "
a.rstrip()
# "hi "

# strip() : remove both left and right whitespace
a = " hi "
a.strip()
# "hi"


##### e.g) with 'flying_circus_cast.txt'
def create_cast_list(filename):
    cast_list = []
    with open(filename) as f:
        for line in f:
            name = line.split(",")[0]
            cast_list.append(name)

    return cast_list

cast_list = create_cast_list('flying_circus_cast.txt')
for actor in cast_list:
    print(actor)
# Graham Chapman
# Eric Idle
# Terry Jones
