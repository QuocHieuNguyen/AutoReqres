import properties
from reqres_auto_test.core.rest_client import RestClient
import properties as prop


class User(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super().__init__(api_root_url, **kwargs)

    def create(self, **kwargs):
        # might be represented as POST method

        return self.post(prop.path_list_users, **kwargs)

    def get_user_list(self, **kwargs):
        # might be represented as GET method

        return self.get(prop.path_list_users, **kwargs)

    def get_user_detail(self, **kwargs):
        # might be represented as GET method

        return self.get(prop.path_list_users, **kwargs)


user = User(properties.root_url)
