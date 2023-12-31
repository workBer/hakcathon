# Generated by Django 4.2.7 on 2023-11-18 14:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(choices=[('MV', 'Кино'), ('CO', 'Концерты'), ('EX', 'Выставки'), ('BK', 'Книги'), ('CR', 'Кафе/Рестораны')], default='MV', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubscribersCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('categories', models.CharField(choices=[('MV', 'Кино'), ('CO', 'Концерты'), ('EX', 'Выставки'), ('BK', 'Книги'), ('CR', 'Кафе/Рестораны')], default='MV', max_length=2)),
                ('header', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('content', models.TextField()),
                ('estimation', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_user', to='social_net.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('comment', models.BooleanField(default=False)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='social_net.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_net.profile')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(through='social_net.SubscribersCategory', to='social_net.profile'),
        ),
    ]
