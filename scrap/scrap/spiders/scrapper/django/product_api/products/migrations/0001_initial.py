# Generated by Django 5.0.6 on 2024-08-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=50)),
                ('availability', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
    ]
