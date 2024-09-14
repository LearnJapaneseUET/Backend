# Generated by Django 5.1.1 on 2024-09-14 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0006_alter_flashcardword_writing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcardword',
            name='writing',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='flashcardword',
            unique_together={('writing', 'meaning', 'furigana')},
        ),
    ]
