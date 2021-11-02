# Illustrates an API call to Datafiniti's Product Database for hotels.
import requests
import urllib.parse
import json

# Set your API parameters here.
API_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJidzBnb2ZxeXM5ZHo3MnRncDdrZDZmOWQ2dzdtbzUwcyIsImlzcyI6ImRhdGFmaW5pdGkuY28ifQ.Qm8429JuC_IdSY6I9S_JL6WW9SGY7GmTrPw7w1p3nT2szoKg7xCM3BtcTfwFYcwKNiDmlfeXNwJnZEEJG5JRlkg1LpbYxZxWaI2ORwibn8jLGIeQiIXW7kXIxR2W4USMZNsutxzNGBOvtylhjmgYhHuqgCFCcwByH0-lvwJF52YE9Yjscual2rHrZfcFbxowaInitMzLx1KtZTfQ-THDjTmgYmZaxyzmXewA83QtqaETjD9Yy0cwfcg2qIG4fr6z4J02ZBZQoNwVdzjj3Z9AUVb_wVZ3Boa0YIznuG9HcKr35vfSTLfPaTLe648ptiiJYlULHCyQbOoR5PpCqJAaAAgkgUXVpD4ECJh6gtp4q-dptBWP6IEWmg_Tjq4jZEB2836PeBtooJdnNCHVQdoAsB0Eugjnuov5Fa-1mkrjMLdlTh0NqXfHTxdD-KXcdUad4Zq3VIy6N4dnqQXWxlaXljQQATPLdHp3X55oapfgTjZ35L8vcvBb0Ucj2dfErASu94QLi6kbrhd86CyNLIGgVJ7lufOiDmKe94PvZ8SBQO0LF_sjhbfGAS76jKQ2oH0nA7V9J8k-4t8dgxpwNIwEpF9GxTSdlayuwdjzE7Uig7nMPMUmDWvuLByYwS0_WbKxPwULnbtMUzRTpNpw3q9fBwqA_0gvb22f-VwJHLWQrGQ'
format = 'JSON'
query = 'postalCode:41011 AND propertyType:"Single Family Dwelling"'
num_records = 1
download = False

request_headers = {
	'Authorization': 'Bearer ' + API_token,
	'Content-Type': 'application/json',
}
request_data = {
    'query': query,
    'format': format,
    'num_records': num_records,
    'download': download
}

# Make the API call.
r = requests.post('https://api.datafiniti.co/v4/properties/search',json=request_data,headers=request_headers)

# Do something with the response.
if r.status_code == 200:
	print(r.content)
else:
	print('Request failed')

filename = 'properties.txt'

records = []

with open(filename) as myFile:
	for line in myFile:
		records.append(json.loads(line))

for record in records:
	# Edit these lines to do more with the data
	print(json.dumps(record['address']))


    # NEXT STEP: NARROWING DOWN JSON DATA