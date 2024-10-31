from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from store_app.models import Order, OrderItems, Product
from account_app.models import Account,UserProfile
from account_app.serializers import UserProfileSerializer


# Create your views here.
User = get_user_model()

class UserProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, user_id):
        profile = get_object_or_404(UserProfile, user__id=user_id)
        data = {
            "full_name": profile.full_name,
            "phone": profile.phone,
            "email": profile.user.email,
            "profile_image": profile.profile_image.url if profile.profile_image else None,
        }
        return JsonResponse(data)
    

class UpdateUserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Ensure only the authenticated user’s profile can be updated
        return self.request.user.userprofile
    
    

@api_view(['POST'])
# @permission_classes(IsAuthenticated)
def submit_order(request):
    try:
        # Retrieve data from request
        cart_items = request.data.get('cartItems')
        payment_method = request.data.get('paymentMethod', 'Cash On Delivery')
        total_amount = request.data.get('totalAmount', 0)

        # Check if cart_items is provided and is a list
        if not cart_items or not isinstance(cart_items, list):
            return Response({"error": "Cart items are missing or invalid."}, status=status.HTTP_400_BAD_REQUEST)

        # Create the order
        order = Order.objects.create(
            customer=request.user,
            total_amount=Decimal(total_amount),
            payment_method=payment_method
        )

        # Create OrderItems
        for item in cart_items:
            product_id = item.get('id')
            quantity = item.get('quantity', 1)
            price = item.get('price', 0)

            if product_id is None or price is None:
                return Response({"error": "Product ID or price is missing in a cart item."}, status=status.HTTP_400_BAD_REQUEST)

            try:
                product = Product.objects.get(id=product_id)
                OrderItems.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=Decimal(price)
                )
            except Product.DoesNotExist:
                return Response({"error": f"Product with ID {product_id} does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Order submitted successfully."}, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)