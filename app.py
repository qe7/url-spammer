import time
import requests
from concurrent.futures import ThreadPoolExecutor

url = str(input("url:\n>"))

amount = int(input("amount:\n> "))
counter = 0

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def profile():
    try:
        with requests.get(url, headers=headers):
            pass  # You can process the response if needed
    except requests.RequestException as e:
        print(f"Error: {e}")


with ThreadPoolExecutor(max_workers=8) as executor:
    for i in range(amount):
        executor.submit(profile)
        counter += 1
        print(f"{counter}/{amount}")
        time.sleep(1.5)  # Throttle the rate of requests
