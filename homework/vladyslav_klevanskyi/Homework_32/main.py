from datetime import datetime
from time import sleep
import requests


print("Stаrt program!")

while True:
    response = requests.get("https://www.google.com")
    print("Status Code: ", response.status_code)
    print(datetime.now())
    sleep(2)
