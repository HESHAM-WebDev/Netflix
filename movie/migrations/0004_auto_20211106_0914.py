# Generated by Django 3.2.9 on 2021-11-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20211105_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
