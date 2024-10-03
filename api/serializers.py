from rest_framework import serializers
from .models import TeamMember, Service, Publication, Review, Search, ContactInformation, About
from .validators import validate_phone_number, validate_email

class TeamMemberSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = TeamMember
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    view_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Service
        fields = '__all__'


class PublicationSerializer(serializers.ModelSerializer):
    team_member = TeamMemberSerializer()

    class Meta:
        model = Publication
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    guid = serializers.UUIDField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class SearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Search
        fields = '__all__'


class ContactInformationSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(validators=[validate_phone_number])
    email = serializers.EmailField(validators=[validate_email])

    class Meta:
        model = ContactInformation
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
