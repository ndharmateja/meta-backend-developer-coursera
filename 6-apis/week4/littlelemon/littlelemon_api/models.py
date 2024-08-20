from django.contrib.auth.models import User
from django.db.models import (
    CASCADE,
    PROTECT,
    SET_NULL,
    BooleanField,
    CharField,
    DateField,
    DecimalField,
    ForeignKey,
    Model,
    SlugField,
    SmallIntegerField,
)


# Create your models here.
class Category(Model):
    slug = SlugField()
    title = CharField(max_length=255, db_index=True)


class MenuItem(Model):
    title = CharField(max_length=255, db_index=True)
    price = DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = BooleanField(db_index=True)
    category = ForeignKey(Category, on_delete=PROTECT)


class Cart(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    menuitem = ForeignKey(MenuItem, on_delete=CASCADE)
    quantity = SmallIntegerField()
    unit_price = DecimalField(max_digits=6, decimal_places=2)
    price = DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ("menuitem", "user")


class Order(Model):
    user = ForeignKey(User, on_delete=CASCADE)
    delivery_crew = ForeignKey(
        User, on_delete=SET_NULL, related_name="delivery_crew", null=True
    )
    status = BooleanField(default=0, db_index=True)
    total = DecimalField(max_digits=6, decimal_places=2, default=0)
    date = DateField(db_index=True)


class OrderItem(Model):
    order = ForeignKey(Order, on_delete=CASCADE, related_name="order")
    menuitem = ForeignKey(MenuItem, on_delete=CASCADE)
    quantity = SmallIntegerField()
    price = DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ("order", "menuitem")
        unique_together = ("order", "menuitem")
