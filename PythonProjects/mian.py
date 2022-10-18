import requests
response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 911,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Рекс",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

import requests
response = requests.put("https://petstore.swagger.io/v2/pet", json={
  "id": 911,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "Rex",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)

import requests
response = requests.get("https://petstore.swagger.io/v2/pet/911", json={
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)