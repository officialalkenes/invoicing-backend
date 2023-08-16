import stripe

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, SubscriptionPlan, Subscription
from .serializers import CustomerSerializer, SubscriptionPlanSerializer
from paypalrestsdk import Payment


class CustomerSubscriptionView(APIView):
    def post(self, request, customer_id, plan_id):
        customer = Customer.objects.get(id=customer_id)
        plan = SubscriptionPlan.objects.get(id=plan_id)

        subscription = Subscription(customer=customer, plan=plan)
        subscription.save()

        # Implement PayPal payment processing here
        # ...

        return Response(
            {"message": "Subscription created successfully."},
            status=status.HTTP_201_CREATED,
        )


class SubscriptionPlanListView(APIView):
    def get(self, request):
        plans = SubscriptionPlan.objects.all()
        serializer = SubscriptionPlanSerializer(plans, many=True)
        return Response(serializer.data)


class PayPalPaymentView(APIView):
    def post(self, request, *args, **kwargs):
        # Initialize PayPal payment
        paypal_payment = Payment(
            {
                "intent": "sale",
                "payer": {"payment_method": "paypal"},
                "transactions": [{"amount": {"total": "10.00", "currency": "USD"}}],
                "redirect_urls": {
                    "return_url": "http://your-website.com/return/",
                    "cancel_url": "http://your-website.com/cancel/",
                },
            }
        )

        if paypal_payment.create():
            return Response({"approval_url": paypal_payment.links[1].href})
        else:
            return Response({"error": "Failed to create PayPal payment"}, status=400)


stripe.api_key = "your-stripe-secret-key"


class StripePaymentView(APIView):
    def post(self, request, *args, **kwargs):
        # Create a Stripe payment
        try:
            payment_intent = stripe.PaymentIntent.create(
                amount=1000,  # Amount in cents
                currency="usd",
                description="Payment for subscription",
                payment_method_types=["card"],
            )
            return Response({"client_secret": payment_intent.client_secret})
        except stripe.error.StripeError as e:
            return Response({"error": str(e)}, status=400)
