from datetime import datetime

from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from .models import (
    Booking,
    ContactMessage,
    Country,
    City,
    Payment,
    Property,
    Review,
    State,
    Tenant,
    Wishlist,
)


def home(request):
    return render(request, "rentalapp/home.html")


def properties(request):
    properties = Property.objects.all()
    return render(request, "rentalapp/properties.html", {
        "properties": properties
    })


def property_detail(request, id):
    property = get_object_or_404(Property, id=id)
    return render(request, "rentalapp/property_detail.html", {
        "property": property
    })


def booking(request, id):

    if "tenant_id" not in request.session:
        return redirect("login")

    property = get_object_or_404(Property, id=id)
    tenant = get_object_or_404(Tenant, id=request.session["tenant_id"])

    if request.method == "POST":

        check_in = request.POST.get("check_in")
        check_out = request.POST.get("check_out")

        check_in_date = datetime.strptime(check_in, "%Y-%m-%d").date()
        check_out_date = datetime.strptime(check_out, "%Y-%m-%d").date()

        total_days = (check_out_date - check_in_date).days

        if total_days <= 0:
            return render(request, "rentalapp/booking.html", {
                "property": property,
                "error": "Check-out date must be after Check-in date."
            })

        total_amount = property.monthly_rent

        booking = Booking.objects.create(
            property=property,
            tenant=tenant,
            check_in=check_in_date,
            check_out=check_out_date,
            total_amount=total_amount,
            booking_status="Pending"
        )

        return redirect("payment", booking.id)

    return render(request, "rentalapp/booking.html", {
        "property": property
    })


def register(request):

    countries = Country.objects.all()
    states = State.objects.all()
    cities = City.objects.all()

    if request.method == "POST":

        Tenant.objects.create(
            country=Country.objects.get(id=request.POST.get("country")),
            state=State.objects.get(id=request.POST.get("state")),
            city=City.objects.get(id=request.POST.get("city")),
            full_name=request.POST.get("full_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            address=request.POST.get("address"),
            password=request.POST.get("password"),
            profile_image=request.FILES.get("profile_image"),
            occupation=request.POST.get("occupation"),
            family_members=request.POST.get("family_members"),
        )

        return redirect("register")

    return render(request, "rentalapp/register.html", {
        "countries": countries,
        "states": states,
        "cities": cities,
    })


def login_view(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            tenant = Tenant.objects.get(
                email=email,
                password=password
            )

            request.session["tenant_id"] = tenant.id
            request.session["tenant_name"] = tenant.full_name

            return redirect("home")

        except Tenant.DoesNotExist:
            return render(
                request,
                "rentalapp/login.html",
                {
                    "error": "Invalid Email or Password"
                }
            )

    return render(request, "rentalapp/login.html")


def my_bookings(request):
    if "tenant_id" not in request.session:
        messages.warning(request, "Please login first.")
        return redirect("login")

    bookings = Booking.objects.filter(
        tenant_id=request.session["tenant_id"]
    )

    return render(
        request,
        "rentalapp/my_bookings.html",
        {
            "bookings": bookings
        }
    )


def wishlist(request):

    if "tenant_id" not in request.session:
        return redirect("login")

    tenant = get_object_or_404(
        Tenant,
        id=request.session["tenant_id"]
    )

    wishlist_items = Wishlist.objects.filter(
        tenant=tenant
    )

    return render(
        request,
        "rentalapp/wishlist.html",
        {
            "wishlist_items": wishlist_items
        }
    )


def add_to_wishlist(request, id):

    if "tenant_id" not in request.session:
        return redirect("login")

    tenant = get_object_or_404(
        Tenant,
        id=request.session["tenant_id"]
    )

    property = get_object_or_404(
        Property,
        id=id
    )

    if not Wishlist.objects.filter(
        tenant=tenant,
        property=property
    ).exists():

        Wishlist.objects.create(
            tenant=tenant,
            property=property
        )

    return redirect("wishlist")


def payment(request, id):

    booking = get_object_or_404(
        Booking,
        id=id
    )

    if request.method == "POST":

        Payment.objects.create(
            booking=booking,
            amount=booking.total_amount,
            payment_method=request.POST.get("payment_method"),
            payment_status="Success",
            transaction_id=f"TXN{booking.id}{booking.tenant.id}"
        )

        return redirect("my_bookings")

    return render(
        request,
        "rentalapp/payment.html",
        {
            "booking": booking
        }
    )


def review(request, id):

    booking = get_object_or_404(
        Booking,
        id=id
    )

    if request.method == "POST":

        Review.objects.create(
            property=booking.property,
            tenant=booking.tenant,
            rating=request.POST.get("rating"),
            review=request.POST.get("review")
        )

        return redirect("my_bookings")

    return render(
        request,
        "rentalapp/review.html",
        {
            "booking": booking
        }
    )


def contact(request):

    if request.method == "POST":

        ContactMessage.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message")
        )

        return redirect("home")

    return render(
        request,
        "rentalapp/contact.html"
    )


def logout_view(request):

    request.session.flush()

    return redirect("home")