# Generated by Django 5.1.2 on 2024-10-25 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrousalHome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('logo_link', models.CharField(default='https://static.vecteezy.com/system/resources/thumbnails/008/174/695/small_2x/loading-circle-icon-loading-gif-loading-screen-gif-loading-spinner-gif-loading-animation-loading-free-video.jpg', max_length=400)),
                ('rating', models.IntegerField(choices=[(1, '#'), (2, '##'), (3, '###'), (4, '####'), (5, '#####')], default=0)),
                ('visiting_link', models.CharField(max_length=200)),
            ],
        ),
    ]
