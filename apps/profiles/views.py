from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import UserProfile, OrganizationProfile
from .serializers import UserProfileSerializer, OrganizationProfileSerializer
from apps.customers.models import Customer
from apps.subscriptions.models import Subscription, SubscriptionPlan


import paypalrestsdk
from paypalrestsdk import Payment


class UserProfileListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk, user=self.request.user)
        except UserProfile.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk, *args, **kwargs):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        user_profile = self.get_object(pk)
        serializer = UserProfileSerializer(user_profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationProfileCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = OrganizationProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(organization=request.user.user_profile)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerSubscriptionView(APIView):
    def post(self, request, customer_id, plan_id):
        customer = Customer.objects.get(id=customer_id)
        plan = SubscriptionPlan.objects.get(id=plan_id)

        subscription = Subscription(customer=customer, plan=plan)
        subscription.save()

        paypalrestsdk.configure(
            {
                "mode": settings.PAYPAL_MODE,
                "client_id": settings.PAYPAL_CLIENT_ID,
                "client_secret": settings.PAYPAL_CLIENT_SECRET,
            }
        )

        payment = Payment(
            {
                "intent": "sale",
                "payer": {"payment_method": "paypal"},
                "redirect_urls": {
                    "return_url": "http://yourdomain.com/success",
                    "cancel_url": "http://yourdomain.com/cancel",
                },
                "transactions": [
                    {
                        "amount": {
                            "total": str(plan.price),
                            "currency": plan.currency,  # Make sure to define currency in SubscriptionPlan model
                        },
                        "description": f"Subscription to {plan.name}",
                    }
                ],
            }
        )

        if payment.create():
            # Save payment ID and customer subscription details to track the payment
            subscription.paypal_payment_id = payment.id
            subscription.save()

            for link in payment.links:
                if link.method == "REDIRECT":
                    redirect_url = link.href
                    return Response(
                        {"redirect_url": redirect_url}, status=status.HTTP_200_OK
                    )
        else:
            return Response(
                {"message": "Payment creation failed"},
                status=status.HTTP_400_BAD_REQUEST,
            )
