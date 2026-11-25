import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# HTTP status codes
def explain_status(code):
    messages = {
        200: "OK - The request succeeded",
        201: "Created - Resource was successfully created",
        400: "Bad Request - Invalid syntax or parameters",
        401: "Unauthorized - Authentication is required",
        404: "Not found",
        500: "Internal Server Error - Something went wrong on the server"
    }
    return messages.get(code, "Unknown status code")

# users
users_response = requests.get(f"{BASE_URL}/users")
if users_response.status_code == 200:
    users = users_response.json()[:5]
    for user in users:
        print(f"{user['id']} - {user['name']} - {user['email']}")

print()  

#POST
new_post = {
    "title": "Sample Post",
    "body": "Learning REST APIs with Python",
    "userId": 1
}
post_response = requests.post(f"{BASE_URL}/posts", json=new_post)
post_data = post_response.json()
print(f"POST: {post_response.status_code}, id: {post_data.get('id')}")

# PUT, PATCH, and DELETE /posts/1
put_response = requests.put(f"{BASE_URL}/posts/1", json={"id": 1, "title": "Updated", "body": "Full update", "userId": 1})
patch_response = requests.patch(f"{BASE_URL}/posts/1", json={"title": "Patched Title"})
delete_response = requests.delete(f"{BASE_URL}/posts/1")

print(f"PUT: {put_response.status_code} | PATCH: {patch_response.status_code} | DELETE: {delete_response.status_code}")

# GET /posts/9999 (404 handling)
not_found_response = requests.get(f"{BASE_URL}/posts/9999")
print(f"GET /posts/9999 -> {not_found_response.status_code} {explain_status(not_found_response.status_code)}")