# Generated by Django 3.0 on 2019-12-05 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, db_index=True, max_length=25, unique=True, verbose_name='Username')),
                ('email', models.CharField(blank=True, db_index=True, max_length=256, unique=True, verbose_name='Email')),
                ('password', models.CharField(blank=True, max_length=128, verbose_name='Password')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'iam_user',
            },
        ),
    ]
