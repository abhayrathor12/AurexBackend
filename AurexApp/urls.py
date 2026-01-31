from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StartupApplicationViewSet,InvestorApplicationViewSet,ContactViewSet,ContactCreateView
from django.conf import settings


router = DefaultRouter()
router.register(r"startups", StartupApplicationViewSet, basename="startups")
router.register(r"investors", InvestorApplicationViewSet, basename="investors")
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [
    path("", include(router.urls)),
    path("con/create/", ContactCreateView.as_view(), name="contact_create"),


]
