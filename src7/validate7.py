# Adds \.edu

import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")


'''
% python validate7.py 
this is an email zewen@abc.edu
it works, need to be changed
'''