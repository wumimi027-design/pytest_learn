def login(username, password):
    fake_db = {
        "admin": "123456",
    }
    if username in fake_db and fake_db[username] == password:
        return {"status": "success"}
    return {"status": "fail"}


def test_login_success(valid_user):
    result = login(valid_user["username"], valid_user["password"])
    assert result["status"] == "success"


def test_login_check_username(valid_user):
    assert valid_user["username"] == "admin"


def test_login_check_password(valid_user):
    assert valid_user["password"] == "123456"

import pytest

@pytest.mark.parametrize("password", [
    "wrong_password",
    "123",
    "",
    "ADMIN123",
])
def test_login_fail(password):
    result = login("admin", password)
    assert result["status"] == "fail"

# def login(username, password):
#     fake_db = {
#         "admin": "123456",
#     }
#     if username in fake_db and fake_db[username] == password:
#         return {"status": "success"}
#     return {"status": "fail"}


# def test_login_success(valid_user):
#     result = login(valid_user["username"], valid_user["password"])
#     assert result["status"] == "success"
