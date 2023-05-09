# Adds character class

import re

email = input("What's your email? ").strip()


'''
[a-zA-Z0-9_] means only a-zA-Z0-9_
'''
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
