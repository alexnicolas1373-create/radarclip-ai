from app.models import User


def test_user_model_defaults():
    user = User()
    assert user.name == ""
    assert user.email == ""
