from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, SubscriptionPlan, Subscription
from .serializers import CustomerSerializer, SubscriptionPlanSerializer


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
