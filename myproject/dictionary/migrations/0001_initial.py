# Generated by Django 5.1 on 2024-08-17 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kanji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('literal', models.CharField(max_length=100)),
                ('stroke_count', models.IntegerField()),
                ('grade', models.IntegerField()),
                ('frequency', models.IntegerField()),
                ('jlpt', models.IntegerField()),
                ('onyomi', models.CharField(max_length=100)),
                ('kunyomi', models.CharField(max_length=100)),
                ('meanings', models.TextField()),
                ('vietnamese', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='KunyomiExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kunyomi_word', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MaziiWordTranslate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=100, unique=True)),
                ('short_mean', models.CharField(max_length=100, unique=True)),
                ('phonetic', models.CharField(max_length=100, unique=True)),
                ('mobileId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OnyomiExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('onyomi_word', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OverallExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m', models.CharField(max_length=255)),
                ('w', models.CharField(max_length=255)),
                ('h', models.CharField(max_length=255)),
                ('p', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WordExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('mean', models.TextField()),
                ('transcription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='KanjiMeaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kanji', models.CharField(max_length=255)),
                ('mean', models.CharField(max_length=255)),
                ('kun', models.CharField(max_length=255)),
                ('on', models.CharField(max_length=255)),
                ('detail', models.TextField()),
                ('mobileId', models.IntegerField()),
                ('stroke_count', models.IntegerField()),
                ('h', models.CharField(max_length=100)),
                ('w', models.CharField(max_length=100)),
                ('example_kun', models.ManyToManyField(to='dictionary.kunyomiexample')),
                ('example_on', models.ManyToManyField(to='dictionary.onyomiexample')),
                ('example', models.ManyToManyField(to='dictionary.overallexample')),
            ],
        ),
        migrations.CreateModel(
            name='MaziiWordKanjiReturnType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('results', models.ManyToManyField(to='dictionary.kanjimeaning')),
            ],
        ),
        migrations.CreateModel(
            name='MaziiWordMeaningReturnType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('found', models.BooleanField()),
                ('data', models.ManyToManyField(to='dictionary.maziiwordtranslate')),
            ],
        ),
        migrations.AddField(
            model_name='onyomiexample',
            name='examples',
            field=models.ManyToManyField(to='dictionary.overallexample'),
        ),
        migrations.AddField(
            model_name='kunyomiexample',
            name='examples',
            field=models.ManyToManyField(to='dictionary.overallexample'),
        ),
        migrations.CreateModel(
            name='SearchField',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result_kanji', models.ManyToManyField(to='dictionary.kanjimeaning')),
                ('result_mazzii', models.ManyToManyField(to='dictionary.maziiwordtranslate')),
            ],
        ),
        migrations.CreateModel(
            name='MaziiWordExampleReturnType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField()),
                ('results', models.ManyToManyField(to='dictionary.wordexample')),
            ],
        ),
        migrations.CreateModel(
            name='WordMeaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mean', models.CharField(max_length=300)),
                ('examples', models.ManyToManyField(to='dictionary.wordexample')),
            ],
        ),
        migrations.AddField(
            model_name='maziiwordtranslate',
            name='means',
            field=models.ManyToManyField(to='dictionary.wordmeaning'),
        ),
    ]
