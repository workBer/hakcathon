# Generated by Django 4.2.7 on 2023-11-22 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_net', '0005_rename_post_rating_post__rating_post_estimation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='_rating',
            field=models.IntegerField(db_column='rating', default=0),
        ),
    ]