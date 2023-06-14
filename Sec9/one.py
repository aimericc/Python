#one.py

def func():
    print("func one in one.py")


print("top level in one.py")

if __name__ == 'main':
    print("one.py is being run directly")
else:
    print("one.py has been imported")
