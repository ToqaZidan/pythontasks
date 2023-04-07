#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer

print(add_integer(1, 5))
print(add_integer(70, -2))
print(add_integer(9))
print(add_integer(110.3, -2))
try:
    print(add_integer(8, "hello"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
   
if __name__ == "__main__":
    import doctest
    doctest.testmode("new.txt")
