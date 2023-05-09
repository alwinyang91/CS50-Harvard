# Uses .group

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), ?(.+)$", name)  # handle one whitespace
# matches = re.search(r"^(.+), *(.+)$", name)  # handle multiple whitespace
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")


'''
Yang,     Zewen now works
'''