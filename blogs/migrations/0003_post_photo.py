# Generated by Django 3.0.8 on 2020-08-31 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20200805_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='/images/default.jpeg', upload_to='images/'),
        ),
    ]
