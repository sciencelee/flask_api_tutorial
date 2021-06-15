
import requests


post_data = [
    {
        0:5,
            },
]

url = 'https://square-flask-api.herokuapp.com/square'
#url = 'http://127.0.0.1:5000/square'

data = requests.post(url, json=post_data)

print(data.text)


url2 = 'https://square-flask-api.herokuapp.com/'
#url2 = 'http://127.0.0.1:5000/'
home = requests.get(url2)
print(home.text)

# with open('static/colleges.txt') as json_file:
#     data = json.load(json_file)


