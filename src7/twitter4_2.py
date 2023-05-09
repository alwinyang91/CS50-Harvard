# Uses capture group

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print("Username:", matches.group(1))  # get the first group

'''
python twitter0.py
https://twitter.com/alwinyang
does not work
'''