# Generated by Django 3.2.21 on 2023-11-19 12:00

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(blank=True, max_length=200)),
                ('company_address', models.CharField(blank=True, max_length=200)),
                ('company_position', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('subject', models.CharField(choices=[('Request Source Code', 'Request Source Code'), ('Reach Out', 'Reach Out'), ('Request Resume', 'Request Resume'), ('Collaborate', 'Collaborate'), ('Chat', 'Chat')], max_length=50)),
                ('message', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.CharField(max_length=200)),
                ('organization', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, default='profile_images/john_Towett_profile.jpeg', null=True, upload_to='profile_images')),
                ('birthday', models.DateField()),
                ('address', models.CharField(max_length=100)),
                ('favorite_programming_languages', models.CharField(max_length=100)),
                ('additional_information', models.TextField()),
                ('occupation', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('experience', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='project_logos/')),
                ('status', models.CharField(choices=[('designing', 'Designing'), ('developing', 'Developing'), ('testing', 'Testing'), ('deploying', 'Deploying'), ('live', 'Live'), ('acquired', 'Acquired')], default='designing', max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('creation_date', models.DateField(default=datetime.date.today)),
                ('acquired_date', models.DateField(blank=True, null=True)),
                ('developers', models.CharField(default='Alex Towett', max_length=100)),
                ('progress', models.PositiveIntegerField(default=10, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('cost', models.PositiveIntegerField(default=20000)),
                ('website', models.URLField(blank=True, default='', null=True)),
                ('source_code', models.URLField(default='https://github.com')),
                ('github_status', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='private', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, default='review_images/default_user.png', help_text='(Optional)', null=True, upload_to='review_images')),
                ('name', models.CharField(max_length=100)),
                ('where_do_you_work', models.CharField(blank=True, max_length=100, null=True)),
                ('what_do_you_do', models.CharField(max_length=100)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('progress', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('projects', models.CharField(max_length=500)),
                ('tools', models.CharField(default='Python', max_length=200)),
            ],
        ),
    ]