from app.config import settings


def test_settings_default_values():
    assert settings.app_name == "RadarClip AI API"
    assert settings.environment == "development"
