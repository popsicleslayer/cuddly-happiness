# Generated by Django 3.0.6 on 2021-03-19 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pet_food_diary', '0002_auto_20210315_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='petmodel',
            name='vet',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vet_name', to=settings.AUTH_USER_MODEL),
        ),
    ]
