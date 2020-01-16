"""
youtube video : https://www.youtube.com/watch?v=sugvnHA7ElY
"""

import first_module
# First Module's Name: first_module

 
##### CASE 1
print("Second Module's Name: {}".format(__name__))

# First Module's Name: first_module
# Second Module's Name: __main__


##### CASE 2 : def main()은 실행되지 않아! 
import first_module
print("Second Module's Name: {}".format(__name__))

"""first_module.py

def main():
    print("First Module's Name: {}".format(__name__))

if __name__ == '__main__': # check, is this file being run directly by Python? or being imported?
    main()

# First Module's Name: __main__
"""
##### output
# Second Module's Name: __main__


##### CASE 3 
import first_module
print("Second Module's Name: {}".format(__name__)) # first_modue.name => first_module.main 블락을 제외한 것들 실행 
# hi
# Run From Import
# bye
# Second Module's Name: __main__

""" first_module.py
print("hi")
if __name__ == '__main__':
    print("Run Directly")
else:
    print("Run From Import")
print("bye")
"""

##### CASE 4 : def main()
import first_module
print("Second Module's Name: {}".format(__name__)) # first_modue.name => first_module.main 블락을 제외한 것들 실행 

# This will always be run
# Second Module's Name: __main__
 
""" first_module.py
print("This will always be run")

def main():
    print("First Module's Main Method")

if __name__ == '__main__':
    print("Inside the name/main")
    main()

# This will always be run
# Inside the name/main
# First Module's Main Method
"""

# If you want to run main() in first_module.py IN second_module.py?
import first_module

first_module.main()

print("Second Module's Name: {}".format(__name__)) # first_modue.name => first_module.main 블락을 제외한 것들 실행 

# This will always be run
# First Module's Main Method
# Second Module's Name: __main__
