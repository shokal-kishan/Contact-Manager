# Generated by Django 4.2.6 on 2023-11-07 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField(primary_key=True, serialize=False)),
            ],
        ),
    ]
