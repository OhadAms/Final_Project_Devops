import requests
import sys

URL = 'http://172.17.0.1:8081/jsp_file_for_final_project.jsp'


url_good(URL)

def url_good(url):
	r = requests.head(url)
	if r.status_code == 200:
		sys.exit(0)
	else:
		sys.exit(1)
