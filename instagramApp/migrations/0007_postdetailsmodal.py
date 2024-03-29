# Generated by Django 4.2.3 on 2023-08-02 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagramApp', '0006_postmodal'),
    ]

    operations = [
        migrations.CreateModel(
            name='postDetailsModal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_user_det', models.CharField(max_length=200)),
                ('post_photo', models.ImageField(upload_to='static/uploaded/posts')),
                ('post_caption', models.CharField(max_length=200)),
                ('post_location', models.CharField(max_length=200)),
                ('post_tag', models.CharField(max_length=200)),
                ('post_time', models.CharField(max_length=200)),
                ('post_comment', models.CharField(max_length=200)),
                ('post_likes', models.CharField(max_length=200)),
                ('post_extra_det1', models.CharField(max_length=200)),
                ('post_extra_det2', models.CharField(max_length=200)),
            ],
        ),
    ]
