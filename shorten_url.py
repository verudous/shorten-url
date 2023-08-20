import requests

url = input("Paste your url here: ")
new_url = requests.get(f'https://is.gd/create.php?format=simple&url={url}')
print(f"New url: {new_url.text}")