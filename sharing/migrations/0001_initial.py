# Generated by Django 4.2.4 on 2023-09-06 15:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '__first__'),
        ('group', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('Message', models.CharField(max_length=255)),
                ('Skill', models.CharField(default='', max_length=20)),
                ('State', models.CharField(default='', max_length=100)),
                ('Photo', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
                ('Video', models.FileField(blank=True, default='', null=True, upload_to='uploads/')),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('Creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Feed',
            },
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='sharing.feed')),
                ('Liker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Likes',
            },
        ),
        migrations.CreateModel(
            name='GroupTimelineComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GrpMessage', models.TextField()),
                ('GrpPictures', models.ImageField(null=True, upload_to='uploads/')),
                ('GrpVideo', models.FileField(null=True, upload_to='uploads/')),
                ('GrpCommenterFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('GrpFeedFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupcomments', to='sharing.feed')),
            ],
            options={
                'db_table': 'GroupTimelineComment',
            },
        ),
        migrations.CreateModel(
            name='GroupTimeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GroupTitle', models.CharField(max_length=255)),
                ('GroupMessage', models.CharField(max_length=255)),
                ('GroupSkill', models.CharField(default='', max_length=20)),
                ('GroupState', models.CharField(default='', max_length=100)),
                ('GroupPhoto', models.ImageField(blank=True, default='', null=True, upload_to='uploads/')),
                ('GroupVideo', models.FileField(blank=True, default='', null=True, upload_to='uploads/')),
                ('Groupcreated_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('CreatorFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('GroupFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='group.group_tbl')),
            ],
            options={
                'db_table': 'GroupTimeline',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Message', models.TextField()),
                ('Pictures', models.ImageField(null=True, upload_to='uploads/')),
                ('Video', models.FileField(null=True, upload_to='uploads/')),
                ('Commenter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='sharing.feed')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='FeedSoilTagging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FeedSoilTag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soilTagging', to='sharing.feed')),
                ('soilTag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.soiltag')),
            ],
            options={
                'unique_together': {('FeedSoilTag', 'soilTag')},
            },
        ),
        migrations.CreateModel(
            name='FeedPlantTagging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FeedPlantTag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plantTagging', to='sharing.feed')),
                ('plantTag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.planttag')),
            ],
            options={
                'unique_together': {('FeedPlantTag', 'plantTag')},
            },
        ),
    ]
