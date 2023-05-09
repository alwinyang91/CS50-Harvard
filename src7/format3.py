# Uses walrus operator

import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), (.+)$", name):  # this is new feature
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
