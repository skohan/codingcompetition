# Generated by Django 3.1.5 on 2021-05-28 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210422_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='solved',
            name='cases_running',
            field=models.BooleanField(default=False),
        ),
    ]