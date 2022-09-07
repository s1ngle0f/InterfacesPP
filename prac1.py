import pprint
import requests

# data = requests.get('https://dog.ceo/api/breeds/image/random')
# data = requests.get('http://numbersapi.com/random/math')
data = requests.get('https://randomuser.me/api/')

pprint.pprint(data)
pprint.pprint(data.json())

###################################################################

