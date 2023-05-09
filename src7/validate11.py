# Adds re.IGNORECASE

import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

'''
now ZEWEN@ABC.EDU works
but ZEWEN@ABC.cs50.EDU does not work
'''