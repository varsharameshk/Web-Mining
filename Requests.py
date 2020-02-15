#Google Search for Tim Berner Lee
import os
import requests

print('====================================================================================================================================================')
r = requests.get('http://www.google.co.in/')
os.startfile('https://www.google.co.in/#q=Tim Berners-Lee')
print('Content of the response:', r.content)
print('Status code of the response:', r.status_code)
print('Response headers:', r.headers)
print('====================================================================================================================================================')


#POST request to a website that does not accept POST requests.
import requests

payload = {'user_name': 'admin', 'password': 'password'}
print('==================================================================================================================================================')
print('This is to demonstrate GET request from the website')
r = requests.get('https://google.com', params=payload)
print(r.url)
print('Content of the response:', type(r))
print('Status code of the response:', r.status_code)
print('Response headers:', r.headers)
print('==================================================================================================================================================')
print('This is to demonstrate POST request not being accepted from the website')
r = requests.post("https://google.com")
print(r.url)
print('Content of the response:', r.content)
print('Status code of the response:', r.status_code)
print('Response headers:', r.headers)
print('==================================================================================================================================================')

#Request to a URL that does not exist.
import requests

print('================================================================================================================================================')
r = requests.post("http://uhfigwiviuviu.com", data={'number': 5000, 'type': 'issue', 'action': 'show'})
print('Content of the response:', r.content)
print('Status code of the response:', r.status_code)
print('Response headers:', r.headers)
print('================================================================================================================================================')
@varsharameshk
 
