import requests

from config.settings.base import env


class ApiError(BaseException):
    pass


def is_valid_email(email):
    access_key = env("MAILBOXLAYER_ACCESS_KEY")
    url = f"http://apilayer.net/api/check?access_key={access_key}&email={email}&smtp=1&format=1"
    r = requests.get(url)
    response = r.json()
    if "success" in response.keys() and not response.get("success"):
        raise ApiError
    if response.get("format_valid") and response.get("mx_found") and response.get("smtp_check"):
        return True
    return False
