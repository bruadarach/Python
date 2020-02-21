'''
# file namemainone.py

def func():
    print("func() in namemainone.py")

print("top-level in namemainone.py")

if __name__ == "__main__":
    print("namemainon.py is being run directly")
else:
    print("namemainone.py is being imported into another module")

# top-level in namemainone.py
# namemainon.py is being run directly
'''


# file two.py
import namemainone # 1 

print("top-level in two.py") # 3 
namemainone.func() # 4

if __name__ == "__main__":
    print("namemaintwo.py is being run directly") # 5
else:
    print("namemaintwo.py is being imported into another module") # 2

# top-level in namemainone.py
# namemainone.py is being imported into another module
# top-level in two.py
# func() in namemainone.py
# namemaintw.py is being run directly