import requests


response = requests.get('https://random-d.uk/api/v2/random')
response2 = requests.get('http://shibe.online/api/shibes?count=1&urls=true&httpsUrls=true')
response3 = requests.get('https://www.fishwatch.gov/api/species/red-snapper')


print(response.json()['url'])
print(response2.json()[0])
print(response3.json()[0]['Location'])