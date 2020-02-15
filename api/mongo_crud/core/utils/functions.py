import random
import string


def random_string(k: int) -> str:
    return ''.join(random.choices(string.ascii_letters, k=k))
