import requests



KEY = open('API_KEY.txt').readlines()
API_KEY = KEY[0]


## Requires API Key from Nasa API: https://api.nasa.gov/
## Can use DEMO_KEY as the key for limited uses
def requestImage(longitude, latitude, dim, API_KEY):
	url = 'https://api.nasa.gov/planetary/earth/imagery?lon=' + str(longitude) + '&lat=' + str(latitude) + '&dim=' +str(dim) + '&api_key=' + API_KEY
	response = requests.request("GET", url)

	file = open('image.png', 'wb')
	file.write(response.content)
	file.close()


if __name__ == "__main__":
	requestImage(-90.365944, 28.738139, 1.0, API_KEY)
	