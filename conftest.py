import pytest

@pytest.fixture(scope="session")
def valid_user():
    data = {"username": "admin", "password": "123456"}
    yield data
    print(f"清理账号: {data['username']}")  # 测试用完了,这时候还能继续用 data 这个变量