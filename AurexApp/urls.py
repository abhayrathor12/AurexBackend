from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from django.conf import settings


router = DefaultRouter()
router.register(r"startups", StartupApplicationViewSet, basename="startups")
router.register(r"investors", InvestorApplicationViewSet, basename="investors")
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'registrations', WebinarRegistrationViewSet, basename='registrations')
urlpatterns = [
    path("", include(router.urls)),
    path("con/create/", ContactCreateView.as_view(), name="contact_create"),

    path('register/', EventRegistrationCreateView.as_view(), name='event-register'),

path("create-order/", CreateOrderView.as_view()),
path("verify-payment/", VerifyPaymentView.as_view()),
]
