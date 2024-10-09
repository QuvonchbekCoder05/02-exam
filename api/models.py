from django.db import models

class Times(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class TeamMember(Times):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    sphere_of_activity = models.TextField()
    education = models.CharField(max_length=200)
    scientific_degree = models.CharField(max_length=100)
    legal_practice = models.TextField()
    license = models.CharField(max_length=100)
    membership = models.CharField(max_length=100)
    languages = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team_member_images/", null=True, blank=True)
    slug = models.SlugField(max_length=400, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Service(Times):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    descriptions = models.TextField()
    image = models.ImageField(upload_to="service_images/", null=True, blank=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Publication(Times):
    title = models.CharField(max_length=200)
    content = models.TextField()
    slug = models.SlugField(unique=True)
    team_member = models.ForeignKey(TeamMember, related_name='publications', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(Times):
    service_id = models.IntegerField()
    full_name = models.CharField(max_length=50)
    description = models.TextField()
    file = models.FileField(upload_to="reviews_files/", null=True, blank=True)
    is_active = models.BooleanField(default=True)
    guid = models.UUIDField(unique=True, editable=False)

    def __str__(self):
        return self.full_name


class Search(Times):
    content_type = models.CharField(max_length=20)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'Search: {self.content_type} - {self.id}'


class ContactInformation(Times):
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    def __str__(self):
        return f'{self.phone_number} - {self.email}'


class About(Times):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    short_description = models.TextField()
    long_description = models.TextField()
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    view_count = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

