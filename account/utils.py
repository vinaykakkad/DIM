import re

from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    """
    Generates token for authentication
    """

    pass


generate_token = TokenGenerator()


def only_letters(answer):
    """Checks if the string contains alpha-numeric characters

    Args:
        answer (string):

    Returns:
        bool:
    """
    match = re.match("^[a-z0-9]*$", answer)
    return bool(match)
