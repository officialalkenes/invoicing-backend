import random
from . import models


def generate_unique_user_id():
    length = 8  # Length of the generated ID excluding the starting '8'
    while True:
        generated_id = "80" + "".join(random.choices("0123456789", k=length))
        if not models.User.objects.filter(pk=generated_id).exists():
            return generated_id
