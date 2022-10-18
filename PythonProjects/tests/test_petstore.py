import imp
from urllib import response
from urllib import response
import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/911')
    assert response.status_code == 200

def test_name():
    response = requests.get("https://petstore.swagger.io/v2/pet/911")
    assert response.json()['name'] == 'Rex'