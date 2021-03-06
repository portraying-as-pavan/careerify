# Generated by Django 3.0.8 on 2020-08-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('company', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=20)),
                ('type_of_place', models.CharField(choices=[('1', 'on-campus'), ('2', 'PPO'), ('3', 'off-campus')], default='1', max_length=20)),
                ('branch', models.CharField(choices=[('1', 'core'), ('2', 'non-core')], default='1', max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
