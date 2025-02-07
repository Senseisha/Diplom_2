import random
import string


def register_new_user():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    email = generate_random_string(7) + "@gmail.com"
    password = generate_random_string(10)
    name = generate_random_string(10)

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    return payload
