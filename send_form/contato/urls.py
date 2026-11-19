from django.urls import path
from . import views

urlpatterns = [
    path("", views.send_contact, name="send_contact"),
    path("obrigado/", views.thank_you, name="thank_you")
]