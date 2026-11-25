import os
import json
import requests
from dotenv import load_dotenv

# environment variables
load_dotenv()

# Read API key
api_key = os.getenv("API_KEY")

# Create headers
headers = {
    "X-API-Key": api_key
}

# Call API and send header
try:
    response = requests.get(
        "https://httpbin.org/headers",
        headers=headers,
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    received_key = data.get("headers", {}).get("X-Api-Key")

    print("Server received key:", received_key)

except requests.exceptions.Timeout:
    print("Request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error occurred")

except requests.exceptions.HTTPError:
    print("HTTP error occurred")


# Handle timeout after 3 seconds
try:
    response = requests.get(
        "https://httpbin.org/delay/10",
        timeout=3
    )

    response.raise_for_status()

except requests.exceptions.Timeout:
    print("Timeout after 3 seconds: please try again")

except requests.exceptions.ConnectionError:
    print("Connection error occurred")


#  Handle server error 500
try:
    response = requests.get(
        "https://httpbin.org/status/500",
        timeout=5
    )

    response.raise_for_status()

except requests.exceptions.HTTPError:
    print("Server error 500 handled")

except requests.exceptions.Timeout:
    print("Server request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error occurred")


# Parse nested JSON response
try:
    response = requests.get(
        "https://httpbin.org/json",
        timeout=5
    )

    response.raise_for_status()

    data = response.json()

    slideshow = data.get("slideshow", {})

    result = {
        "title": slideshow.get("title"),
        "author": slideshow.get("author"),
        "slides": slideshow.get("slides", [])
    }

    #  Save data into JSON file
    with open("result.json", "w") as file:
        json.dump(result, file, indent=4)

    print("JSON data saved successfully")

except requests.exceptions.Timeout:
    print("JSON request timed out")

except requests.exceptions.ConnectionError:
    print("Connection error occurred")

except requests.exceptions.HTTPError:
    print("HTTP error occurred")