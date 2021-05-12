import re

from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    pass

generate_token = TokenGenerator()


def only_letters(answer):
	'''
		Checks if the answer only contains lowercase english alphabets
	'''
	match = re.match("^[a-z0-9]*$", answer)
	return bool(match)