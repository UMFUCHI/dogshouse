import requests
import time
from fake_useragent import UserAgent
from datetime import datetime
import sys

fake_useragent = UserAgent()

url = "https://api.onetime.dog/rewards"


with open('id.txt', 'r') as file:
    user_ids = file.read().splitlines()
with open('proxies.txt', 'r') as file:
    proxies = file.read().splitlines()
with open('useragent.txt', 'r') as file:
    useragent = file.read().splitlines()

current_time = datetime.now().strftime("%a, %d %b %Y %H:%M:%S")
total = 0

for i in range(len(user_ids)):
    proxy = {
        "http": f'http://{proxies[i]}'
    }

    params = {
        'user_id': user_ids[i]
    }

    headers = {
        'User-Agent': useragent[i],
        'Accept': "application/json",
        'sec-ch-ua': "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Android WebView\";v=\"126\"",
        'sec-ch-ua-mobile': "?1",
        'sec-ch-ua-platform': "\"Android\"",
        'origin': "https://onetime.dog",
        'x-requested-with': "org.telegram.messenger",
        'sec-fetch-site': "same-site",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://onetime.dog/",
        'accept-language': "en,id-ID;q=0.9,id;q=0.8,en-US;q=0.7",
        'if-modified-since': current_time,
        'priority': "u=1, i"
    }

    sys.stdout.flush()
    response = requests.get(url, params=params, headers=headers, proxies=proxy)
    print(f"{i+1}. Response for user_id {user_ids[i]}:")
    print(response.text)
    sys.stdout.flush()
    sys.stdout.flush()
    total = total + int(response.json()['total'])
    # time.sleep(3)

print(f'Total points: {total}')
