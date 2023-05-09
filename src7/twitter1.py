# Extracts Twitter username from URL using str.removeprefix

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")


'''
python twitter0.py
my username is https://twitter.com/alwinyang

still does not work
'''