# Generated by Django 4.2.7 on 2023-11-21 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social_net', '0003_remove_category_subscribers_profile_subscribers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_user', related_query_name='post_user', to='social_net.profile'),
        ),
    ]
