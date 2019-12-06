import random
import string


def generator(size=6):
    rand_str = ''.join(random.choices(string.ascii_letters + string.digits, k=size))
    return rand_str
