# Generated by Django 3.2.18 on 2023-06-22 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_data', models.ImageField(upload_to='images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=40)),
                ('first_name', models.CharField(max_length=90)),
                ('last_name', models.CharField(max_length=90)),
                ('Age', models.IntegerField()),
                ('Height', models.FloatField(max_length=200)),
                ('Weight', models.FloatField(max_length=200)),
                ('Gender', models.FloatField(max_length=200)),
                ('Ethnicity', models.FloatField(max_length=200)),
                ('Hydration', models.FloatField()),
                ('date', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=40)),
                ('date', models.DateTimeField()),
                ('activity', models.IntegerField()),
                ('work_time', models.IntegerField()),
                ('Hydration', models.FloatField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
