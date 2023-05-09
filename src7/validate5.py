# Adds .*

import re

email = input("What's your email? ").strip()

if re.search(".*@.*", email):
    print("Valid")
else:
    print("Invalid")


'''
% python validate5.py zewen@
it works because * include 0 str
should use +
'''