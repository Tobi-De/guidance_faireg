import re

from django.core.exceptions import ValidationError


def get_operator(phone_number):
    """
    return MTN or MOOV based on the phone number use
    """
    mtn_prefixes = ["97", "96", "66", "67", "61", "62", "69", "91", "90", "51"]
    moov_prefixes = ["68", "98", "99", "95", "94", "60", "64", "63", "65"]
    prefixe = phone_number[0:2]
    if prefixe in mtn_prefixes:
        return "MTN"
    elif prefixe in moov_prefixes:
        return "MOOV"
    else:
        return None


def validate_phone_number(value):
    if not get_operator(value):
        raise ValidationError("Invalide numéro, nous avons besoin d'un numero MOOV ou MTN")
    phone_number_pattern = re.compile(r"\d{8}")
    if not phone_number_pattern.fullmatch(value):
        raise ValidationError("Numéro de téléphone invalide")
