# Adds error checking

import sys

if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
    print("Too many arguments")


print("hello, my name is", sys.argv[1])


'''
problem is that when there is no input, the code brokes
'''