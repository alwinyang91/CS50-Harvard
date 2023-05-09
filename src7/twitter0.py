# Extracts Twitter username from URL using str.replace

url = input("URL: ").strip()

username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")


'''
python twitter0.py
https://twitter.com/alwinyang

but my username is https://twitter.com/alwinyang
does not work
'''