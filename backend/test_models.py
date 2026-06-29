from app.models import User


def test_user_model_defaults():
    user = User(email="test@example.com", name="Test User", hashed_password="hash")
    assert user.name == "Test User"
    assert user.email == "test@example.com"
