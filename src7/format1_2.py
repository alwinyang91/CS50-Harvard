# Uses re.search

import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), (.+)$", name)  # () can capture str in ()

if matches:
    last = matches.groups(1)
    first = matches.groups(2)
    name = first + " " + last
print(f"hello, {name}")


