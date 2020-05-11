# Generated by Django 3.0.4 on 2020-05-11 01:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Voting', '0002_vote_votetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='voters',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
