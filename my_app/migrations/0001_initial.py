# Generated by Django 3.0.3 on 2020-03-11 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(blank=True, max_length=500)),
                ('created', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
