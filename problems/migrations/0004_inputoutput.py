# Generated by Django 3.1.2 on 2021-04-17 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_problem_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputOutput',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('input_data', models.TextField()),
                ('output_data', models.TextField()),
                ('problem_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.problem')),
            ],
        ),
    ]
