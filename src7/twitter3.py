# Allows for http, no protocol, and www.

import re

url = input("URL: ").strip()

'''
username = re.sub(r"^(http|https)://twitter\.com/", "", url)  # now http can be tolerated
username = re.sub(r"^https?://twitter\.com/", "", url)  # the same
username = re.sub(r"^https?://(www\.)?twitter\.com/", "", url)  # now www. can be tolerated
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)  # now https?:// can be tolerated
'''
username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}")
