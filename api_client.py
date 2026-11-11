import requests

api_url = "https://api.github.com"
json_keys = ("current_user_url", "repository_url", "user_url")

try:
    response = requests.get(api_url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as error:
    print("Request failed:", error)
else:
    print("Status code:", response.status_code)
    print("Content-Type:", response.headers.get("Content-Type"))

    if "application/json" in response.headers.get("Content-Type", ""):
        data = response.json()
        for key in json_keys:
            if key in data:
                print(f"{key}: {data[key]}")
    else:
        print("Response was not JSON, not printing keys.")
