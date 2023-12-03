from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

DESIGNING = 'designing'
DEVELOPING = 'developing'
TESTING = 'testing'
DEPLOYING = 'deploying'
LIVE = 'live'
ACQUIRED = 'acquired'
PUBLIC = 'public'
PRIVATE = 'private'

PROJECT_STATUS_CHOICES = [
    (DESIGNING, 'Designing'),
    (DEVELOPING, 'Developing'),
    (TESTING, 'Testing'),
    (DEPLOYING, 'Deploying'),
    (LIVE, 'Live'),
    (ACQUIRED, 'Acquired'),
]

GITHUB_STATUS_CHOICES = [
    ('public', 'Public'),
    ('private', 'Private'),
]


# Define your project model
class Project(models.Model):
    logo = models.ImageField(upload_to='project_logos/')
    status = models.CharField(max_length=10, choices=PROJECT_STATUS_CHOICES, default=DESIGNING)
    name = models.CharField(max_length=100)
    description = models.TextField()
    creation_date = models.DateField(default=date.today)
    acquired_date = models.DateField(blank=True, null=True)
    developers = models.CharField(max_length=100, default='Alex Towett')
    progress = models.PositiveIntegerField(default=10, validators=[
        MaxValueValidator(100),
        MinValueValidator(0)])  # Default progress set to 10%
    cost = models.PositiveIntegerField(default=20000)
    website = models.URLField(default="", blank=True, null=True)
    source_code = models.URLField(default="https://github.com")
    github_status = models.CharField(max_length=10, choices=GITHUB_STATUS_CHOICES, default='private')

    def __str__(self):
        return self.name


class Profile(models.Model):
    profile_image = models.ImageField(
        blank=True, null=True, upload_to='profile_images',
        default='profile_images/john_Towett_profile.jpeg'
    )
    birthday = models.DateField()
    address = models.CharField(max_length=100)
    favorite_programming_languages = models.CharField(max_length=100)
    additional_information = models.TextField()
    occupation = models.CharField(max_length=100)
    skills = models.CharField(max_length=100)
    experience = models.PositiveIntegerField()

    def age(self):
        today = date.today()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age


class Review(models.Model):
    profile_photo = models.ImageField(blank=True, null=True, upload_to='review_images',
                                      default='review_images/default_user.png', help_text='(Optional)')
    name = models.CharField(max_length=100)
    where_do_you_work = models.CharField(max_length=100, null=True, blank=True)
    what_do_you_do = models.CharField(max_length=100)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Milestone(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=200)
    organization = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Skill(models.Model):
    name = models.CharField(max_length=100)
    progress = models.IntegerField(default=0, validators=[
        MaxValueValidator(100),
        MinValueValidator(0)])
    projects = models.CharField(max_length=500)
    tools = models.CharField(max_length=200, default='Python')

    def __str__(self):
        return self.name


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200, blank=True)
    company_address = models.CharField(max_length=200, blank=True)
    company_position = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20, blank=True)
    SUBJECT_CHOICES = [
        ('Request Source Code', 'Request Source Code'),
        ('Reach Out', 'Reach Out'),
        ('Request Resume', 'Request Resume'),
        ('Collaborate', 'Collaborate'),
        ('Chat', 'Chat'),
    ]
    subject = models.CharField(max_length=50, choices=SUBJECT_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}"
