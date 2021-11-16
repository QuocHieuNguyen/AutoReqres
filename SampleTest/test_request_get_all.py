import requests
import pytest

ROOT_URL = "https://reqres.in"
def get_list_user():
    url = ROOT_URL + "/api/users?page=2"
    response = requests.get(url)
    print(response)
    print(dir(response))
    print(response.json())
# get_list_user()

def post_create_user():
    url = ROOT_URL + "/api/users"
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    res = requests.post(url, data)
    print(res)
    print(res.json())
#post_create_user()
def update_user_by_put_method():
    url = ROOT_URL + "/api/users/2"
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    res = requests.put(url, data)
    print(res)
    print(res.json())
#update_user_by_put_method()
def delete_user_by_delete_method():
    url = ROOT_URL + "/api/users/2"
    res = requests.delete(url)
    print(res)
#delete_user_by_delete_method()
def update_user_by_patch_method():
    url = ROOT_URL + "/api/users/2"
    data = {
        "name": "morpheus",
        "job": "zion resident"
    }
    res = requests.patch(url, data)
    print(res)
    print(res.json())
update_user_by_patch_method()