from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.urls import path

from . import views
from .views import CustomPasswordResetView

urlpatterns = [
    path("sign_in/", views.sign_in, name="sign_in"),
    path("sign_up/", views.sign_up, name="sign_up"),
    path("", views.index, name="index"),
    path("success/", views.success, name="success"),
    path("reservation/", views.reservation, name="reservation"),
    path("about/", views.about, name="about"),
    path("profile/", views.profile, name="profile"),
    path("contact/", views.contact, name="contact"),
    path("attractions/", views.attractions, name="attractions"),
    path("reservation_summary/", views.reservation_summary, name="reservation_summary"),
    path("logout/", LogoutView.as_view(template_name="logout.html"), name="logout"),
    path("docs/", views.docs_view, name="docs"),
    path("reservation_lookup/", views.reservation_lookup, name="reservation_lookup"),
    path("my-reservations/", views.reservation_history, name="reservation_history"),
    path("past-reservations/", views.past_reservations, name="past_reservations"),
    path("future-reservations/", views.future_reservations, name="future_reservations"),
    path("create-reservation/", views.create_reservation, name="create_reservation"),
    path("room_rates/", views.room_rates, name="room_rates"),
    path("reservation-lookup/", views.reservation_lookup, name="reservation_lookup"),
    path(
        "reservation_lookup_results/",
        views.reservation_lookup_results,
        name="reservation_lookup_results",
    ),
    path("password_reset/", views.password_reset, name="password_reset"),
    path("password_reset_done/", views.password_reset_done, name="password_reset_done"),
    path("password_reset/", CustomPasswordResetView.as_view(), name="password_reset"),
    path(
        "restaurant-reservation/",
        views.restaurant_reservation,
        name="restaurant_reservation",
    ),
]
