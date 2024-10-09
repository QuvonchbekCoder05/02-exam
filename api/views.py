from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .models import TeamMember, Service, Publication, Review, Search, ContactInformation, About,News
from .serializers import (
    TeamMemberSerializer, ServiceSerializer, PublicationSerializer, ReviewSerializer, 
    SearchSerializer, ContactInformationSerializer, AboutSerializer,NewsSerializer
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


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().order_by('-created_time')
    serializer_class = NewsSerializer
    lookup_field = 'slug'
    
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['view_count']
    search_fields = ['title', 'short_description', 'long_description']
    ordering_fields = ['created_time', 'view_count']
