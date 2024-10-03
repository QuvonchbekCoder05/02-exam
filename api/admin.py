from django.contrib import admin
from .models import TeamMember, Service, Publication, Review, Search, ContactInformation, About

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'slug')
    search_fields = ('first_name', 'last_name', 'position')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'view_count', 'created_time')
    search_fields = ('title', 'descriptions')

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'team_member', 'slug')
    search_fields = ('title', 'content')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'service_id', 'is_active', 'created_time')
    search_fields = ('full_name', 'description')

@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'id')
    search_fields = ('content_type', 'id')

@admin.register(ContactInformation)
class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'email')
    search_fields = ('phone_number', 'email')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_time', 'updated_time')
    search_fields = ('title',)
