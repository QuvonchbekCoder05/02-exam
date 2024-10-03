from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import TeamMember, Service, Publication, Review, Search, ContactInformation, About
from .serializers import (
    TeamMemberSerializer, ServiceSerializer, PublicationSerializer, ReviewSerializer, 
    SearchSerializer, ContactInformationSerializer, AboutSerializer
)

class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['first_name', 'last_name', 'position', 'sphere_of_activity']


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'descriptions']


class PublicationViewSet(viewsets.ModelViewSet):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'content', 'team_member__first_name', 'team_member__last_name']


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class SearchViewSet(viewsets.ModelViewSet):
    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    filter_backends = [SearchFilter]
    search_fields = ['content_type', 'id']


class ContactInformationViewSet(viewsets.ModelViewSet):
    queryset = ContactInformation.objects.all()
    serializer_class = ContactInformationSerializer


class AboutViewSet(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
