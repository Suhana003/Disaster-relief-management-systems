# Generated by Django 5.1.6 on 2025-02-28 05:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relief', '0002_missingperson_rename_name_volunteer_fullname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='photo',
            field=cloudinary.models.CloudinaryField(default='80e573ee1f1ef0fa0a70633ebfd74c54_a8xzti', max_length=255, verbose_name='image'),
        ),
    ]
