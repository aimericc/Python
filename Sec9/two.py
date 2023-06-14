#two.py

import one

print("top level in two.py")

one.func()

if __name__ == 'main':
    print("two.py is being run directly")
else:
    print("two.py has been imported")
