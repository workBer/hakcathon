# Generated by Django 4.2.7 on 2023-11-15 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_net', '0002_alter_post_photo_alter_profile_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]