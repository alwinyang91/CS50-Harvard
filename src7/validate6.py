# Changes * to +

import re

email = input("What's your email? ").strip()

# if re.search("..*@..*", email):
# if re.search(".{1}.*@.{1}.*", email):
if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")
