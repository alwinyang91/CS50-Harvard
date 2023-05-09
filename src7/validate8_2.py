# Adds ^ and $ to regex

import re

email = input("What's your email? ").strip()


'''
[^@] means any character except @
'''
if re.search(r"^[^@]+@[^@]\.edu$", email):
    print("Valid")
else:
    print("Invalid")
