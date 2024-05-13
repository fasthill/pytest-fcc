import pytest
import source.service as service

import unittest.mock as mock

@mock.patch("source.service.get_user_from_db") # 테스트하고자 하는 파일의 path
def test_get_user_from_db(mock_get_user_from_db): # 다른 이름을 사용해도 됨. 반드시 같을 필요 없음.
    mock_get_user_from_db.return_value = "Mocked Alice" # Mocked Alice를 리턴받는다고 mocking함
    user_name = service.get_user_from_db(1)
    print(f"user_name: {user_name}")
    assert user_name == "Mocked Alice"