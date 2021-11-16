import pytest
import requests
from reqres_auto_test.operations import ops_user as User


class TestUser:

    def test_create_user(self):
        # default id, but in this case, this is a POST method
        # for creating a new user, so id may not be needed
        _id = 1
        response = User.create_user(_id)
        print(response.text)
        assert response.status_code is 201, f"The test is failed, the actual status code is {response.status_code}"
