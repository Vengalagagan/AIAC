import unittest
import string

def is_valid_email(email):
    # Validate type and non-empty
    if not isinstance(email, str) or not email:
        return False

    # Check for exactly one '@'
    if email.count('@') != 1:
        return False

    # Must contain at least one '.'
    if '.' not in email:
        return False

    # Must not start or end with special characters
    special_chars = set(string.punctuation)
    if email[0] in special_chars or email[-1] in special_chars:
        return False

    # '@' and '.' must not be at the start or end
    if email[0] in {'@', '.'} or email[-1] in {'@', '.'}:
        return False

    # Validate local and domain parts around '@'
    local_part, domain_part = email.split('@')
    if not local_part or not domain_part:
        return False

    # '.' must not be at the start or end of local or domain parts
    if local_part[0] == '.' or local_part[-1] == '.':
        return False
    if domain_part[0] == '.' or domain_part[-1] == '.':
        return False

    return True
  



