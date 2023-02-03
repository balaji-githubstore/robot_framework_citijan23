import  requests

# BASE_URL="https://petstore.swagger.io/v2"

response=requests.get(url="https://petstore.swagger.io/v2/pet/20051")
print(response)
print(response.status_code)
print(response.json())
print(response.json()["id"])