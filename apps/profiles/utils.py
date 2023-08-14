import random


def generate_unique_id():
    length = 8  # Length of the generated ID excluding the starting '8'
    while True:
        generated_id = "80" + "".join(random.choices("0123456789", k=length))
        from .models import OrganizationProfile

        if not OrganizationProfile.objects.filter(pk=generated_id).exists():
            return generated_id


def user_directory_path(instance, filename):
    # Define the file upload path
    return f"user_{instance.user.id}/{filename}"
