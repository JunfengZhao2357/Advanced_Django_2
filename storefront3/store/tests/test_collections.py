from rest_framework import status
from rest_framework.test import APIClient
import pytest

@pytest.mark.django_db
class TestCreateCollection:
    # the following decorator will skip the specific test
    # @pytest.mark.skip
    def test_if_user_is_anonymous_returns_401(self):
        # every test should consider the following three parts
        # AAA (Arrange, Act, Assert)
        # Arange (None)
        
        # Act
        client =  APIClient()
        response = client.post('/store/collections/', {'title': 'a'})
        
        # Assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED