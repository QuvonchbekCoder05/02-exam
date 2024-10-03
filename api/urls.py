from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TeamMemberViewSet, ServiceViewSet, PublicationViewSet, ReviewViewSet, 
    SearchViewSet, ContactInformationViewSet, AboutViewSet
)

router = DefaultRouter()
router.register(r'team-member', TeamMemberViewSet, basename='team-member')
router.register(r'services', ServiceViewSet, basename='services')
router.register(r'publications', PublicationViewSet, basename='publications')
router.register(r'reviews', ReviewViewSet, basename='reviews')
router.register(r'search', SearchViewSet, basename='search')
router.register(r'contact-information', ContactInformationViewSet, basename='contact-information')
router.register(r'about', AboutViewSet, basename='about')

urlpatterns = [
    path('', include(router.urls)),
]
