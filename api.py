import requests

# Cloudflare Worker URL
url = "https://start-api-phonetracker.dev-lorenzo.workers.dev"

def check_api(url):

    try:
        response = requests.get(url, timeout=5)
        status = response.status_code
        return 200 <= status < 300
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)
        return False

# Call the function and store result in api_success
api_success = check_api(url)
