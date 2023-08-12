from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import redirect

from celery import shared_task
from PIL import Image
from .models import UserProfile, OrganizationProfile


@shared_task
def send_email(request):
    recipient_email = "example@example.com"
    recipient_name = "John Doe"
    confirmation_token = "abc123"  # Unique token for the email

    subject = "Welcome to Our Newsletter"
    message = render_to_string(
        "email_template.html",
        {
            "recipient_name": recipient_name,
            "tracker_url": request.build_absolute_uri(f"/track/{confirmation_token}"),
            "tracking_pixel": request.build_absolute_uri(
                f"/pixel/{confirmation_token}.gif"
            ),
        },
    )

    email = EmailMessage(subject, message, to=[recipient_email])
    email.content_subtype = "html"  # Set the email content type as HTML
    email.send()


def track_email(request, token):
    # Update your database or perform actions based on the tracked email
    # You can store the token in your database and mark the email as viewed

    # Redirect the user to a specific page or display a message
    return redirect("confirmation_page")


@shared_task
def onboard_user(user_id):
    user_profile = UserProfile.objects.get(user_id=user_id)
    user_profile.is_onboarded = True
    user_profile.save()


@shared_task
def process_logo(organization_profile_id):
    org_profile = OrganizationProfile.objects.get(id=organization_profile_id)

    if org_profile.logo:
        image = Image.open(org_profile.logo.path)
        # Perform any image processing using PIL here
        # For example, resizing the image
        resized_image = image.resize((100, 100), Image.ANTIALIAS)

        # Save the processed image back
        resized_image.save(org_profile.logo.path)
