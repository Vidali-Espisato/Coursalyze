# Generated by Django 2.2.6 on 2019-10-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('course_url', models.URLField()),
                ('description', models.TextField()),
                ('instructor', models.CharField(max_length=50)),
                ('min_price', models.IntegerField()),
                ('max_price', models.IntegerField()),
                ('prerequisites', models.TextField()),
                ('skills_gained', models.TextField()),
                ('rating', models.FloatField(blank=True, null=True)),
                ('duration', models.FloatField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('enroll_by', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_text', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Searches',
            },
        ),
    ]