from django.contrib.auth.models import User
from rest_framework.serializers import (
    CurrentUserDefault,
    ModelSerializer,
    PrimaryKeyRelatedField,
)

from .models import Cart, Category, MenuItem, Order, OrderItem


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "title", "slug"]


class MenuItemSerializer(ModelSerializer):
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = MenuItem
        fields = ["id", "title", "price", "category", "featured"]


class CartSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(
        queryset=User.objects.all(), default=CurrentUserDefault()
    )

    def validate(self, attrs):
        attrs["price"] = attrs["quantity"] * attrs["unit_price"]
        return attrs

    class Meta:
        model = Cart
        fields = ["user", "menuitem", "unit_price", "quantity", "price"]
        extra_kwargs = {"price": {"read_only": True}}


class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ["order", "menuitem", "quantity", "price"]


class OrderSerializer(ModelSerializer):
    orderitem = OrderItemSerializer(many=True, read_only=True, source="order")

    class Meta:
        model = Order
        fields = ["id", "user", "delivery_crew", "status", "date", "total", "orderitem"]


class UserSerilializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]
        fields = ["id", "username", "email"]

    class Meta:
        model = User
        fields = ["id", "username", "email"]
        fields = ["id", "username", "email"]
