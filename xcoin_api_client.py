import os
import requests

def xcoinApiCall(url, rgParams):
	api_url = "https://api.bithumb.com" + url

	response = requests.get(api_url, params=rgParams)

	print("status code: ", response.status_code)

	return response
