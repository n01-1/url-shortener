# Generated by Django 3.0 on 2019-12-05 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shortener_iam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='client', related_query_name='client', serialize=False, to='shortener_iam.User')),
                ('long_url', models.CharField(blank=True, max_length=512, verbose_name='Long URL')),
                ('short_url', models.CharField(blank=True, max_length=256, verbose_name='Short URL')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'client_client',
            },
        ),
    ]
