# Generated by Django 5.0.2 on 2024-03-03 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
