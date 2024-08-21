import json
from datetime import datetime

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from . import forms, models


# Create your views here.
def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def reservations(request):
    bookings = models.Booking.objects.all()
    bookings_data = {"bookings": bookings}
    return render(request, "restaurant/bookings.html", {"bookings": bookings_data})


def book(request):
    form = forms.BookingForm()
    if request.method == "POST":
        form = forms.BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "restaurant/book.html", context)


def menu(request):
    menu_data = models.Menu.objects.all()
    main_data = {"menu": menu_data}
    return render(request, "restaurant/menu.html", {"menu": main_data})


def display_menu_item(request, pk=None):
    if pk:
        menu_item = models.Menu.objects.get(pk=pk)
    else:
        menu_item = ""
    return render(request, "restaurant/menu_item.html", {"menu_item": menu_item})


@csrf_exempt
def bookings(request):
    if request.method == "POST":
        data = json.load(request)
        exist = (
            models.Booking.objects.filter(reservation_date=data["reservation_date"])
            .filter(reservation_slot=data["reservation_slot"])
            .exists()
        )
        if exist == False:
            booking = models.Booking(
                first_name=data["first_name"],
                reservation_date=data["reservation_date"],
                reservation_slot=data["reservation_slot"],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type="application/json")

    date = request.GET.get("date", None)
    if date is not None:
        bookings = models.Booking.objects.all().filter(reservation_date=date)
    else:
        bookings = models.Booking.objects.all()

    booking_json = serializers.serialize("json", bookings)

    return HttpResponse(booking_json, content_type="application/json")
