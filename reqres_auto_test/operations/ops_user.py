from reqres_auto_test.api.user import user
# import * means import all
from reqres_auto_test.payload.payload_user import *


def create_user(id, cookie = None):
    # the parameter cookie is still under consideration
    created_user = user.create(
        json=payload_create_user(id),
        headers={
            'Content-Type': 'application/json; charset=UTF-8'
        },
        cookies=cookie
    )
    return created_user
