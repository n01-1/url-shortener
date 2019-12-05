from django.db import models


class User(models.Model):
    username = models.CharField('Username', max_length=25, blank=True, unique=True, db_index=True)
    email = models.CharField('Email', max_length=256, blank=True, unique=True, db_index=True)
    password = models.CharField('Password', max_length=128, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'iam_user'


