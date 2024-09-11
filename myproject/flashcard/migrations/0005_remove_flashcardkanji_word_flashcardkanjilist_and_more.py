# Generated by Django 5.1.1 on 2024-09-11 03:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0004_rename_list_id_flashcardlist_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcardkanji',
            name='word',
        ),
        migrations.CreateModel(
            name='FlashcardKanjiList',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('word', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='kanjilist', to='flashcard.flashcardword')),
            ],
        ),
        migrations.AddField(
            model_name='flashcardkanji',
            name='kanjilist',
            field=models.ManyToManyField(related_name='kanjis', to='flashcard.flashcardkanjilist'),
        ),
    ]
