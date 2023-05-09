# Uses re.sub

import re

url = input("URL: ").strip()

username = re.sub(r"^https://twitter\.com/", "", url)
print(f"Username: {username}")


'''
python twitter0.py
my username is https://twitter.com/alwinyang

still does not work
'''