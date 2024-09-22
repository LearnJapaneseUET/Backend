# Generated by Django 5.1 on 2024-08-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0006_comment_delete_kanji_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w', models.CharField(max_length=200)),
                ('m', models.CharField(max_length=200)),
                ('p', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=10, unique=True)),
                ('readings', models.ManyToManyField(related_name='kanji', to='dictionary.reading')),
            ],
        ),
    ]