# Generated by Django 5.1 on 2024-08-27 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0011_alter_extractkanjilist_word_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flashcardkanji',
            name='kanji_id',
        ),
        migrations.RemoveField(
            model_name='flashcardword_list',
            name='list_id',
        ),
        migrations.AlterField(
            model_name='flashcardword',
            name='word_id',
            field=models.CharField(default='None', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='flashcardkanji',
            name='id',
            field=models.CharField(default='None', max_length=10, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='flashcardlist',
            name='word_list',
            field=models.ManyToManyField(to='dictionary.flashcardword'),
        ),
        migrations.AddField(
            model_name='flashcardword',
            name='kanji_list',
            field=models.ManyToManyField(to='dictionary.flashcardkanji'),
        ),
        migrations.AlterField(
            model_name='flashcardlist',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='ExtractKanjiList',
        ),
        migrations.DeleteModel(
            name='FlashcardWord_list',
        ),
    ]
