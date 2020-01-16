"""
youtube video : https://www.youtube.com/watch?v=sugvnHA7ElY
"""

##### Special Variable : 'name'

##### We can run the module inside the file
"""
print(__name__)
# __main__

print("First Module's Name: {}".format(__name__))
# First Module's Name: __main__
"""

##### We can also import the module into another file
"""
def main():
    print("First Module's Name: {}".format(__name__))

if __name__ == '__main__': # check, is this file being run directly by Python? or being imported?
    main()
# First Module's Name: __main__
"""

##### Make it clear?
"""
print("hi")
if __name__ == '__main__':
    print("Run Directly")
else:
    print("Run From Import")
print("bye")
# hi
# Run Directly
# bye
"""

##### def main()
"""
print("This will always be run")

def main():
    print("First Module's Main Method")

if __name__ == '__main__':
    main()
# This will always be run
# First Module's Main Method
"""


print("This will always be run")

def main():
    print("First Module's Main Method")

if __name__ == '__main__':
    print("Inside the name/main")
    main()
# This will always be run
# Inside the name/main
# First Module's Main Method

