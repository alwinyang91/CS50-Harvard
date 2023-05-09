# Uses capture group

import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)  # now, the group (?:) will be ignored
if matches:
    print("Username:", matches.group(1))  # get the first group
