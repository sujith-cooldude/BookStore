# Generated by Django 3.2.15 on 2022-08-31 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='longDescription',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='pageCount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='shortDescription',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='thumbnailUrl',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
