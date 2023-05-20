from django.db import models
from django.contrib.auth.models import User
from storages.backends.s3boto3 import S3Boto3Storage


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'id = {self.id}, first_name = {self.first_name}, last_name = {self.last_name}, surname = {self.surname}'


class S3StorageClass(S3Boto3Storage):
    bucket_name = 'krbackend'
    location = 'media'
    file_overwrite = False  # Если запретить перезапись файлов


class Article(models.Model):
    name_article = models.CharField(max_length=255, blank=True, null=True)
    author = models.ForeignKey('Author', on_delete=models.PROTECT, null=True)
    appeal = models.CharField(max_length=255, blank=True, null=True)
    notification = models.CharField(max_length=255, blank=True, null=True)
    year_of_publication = models.DateTimeField(blank=True, null=True)
    theme = models.CharField(max_length=255, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    url_article = models.CharField(max_length=255, blank=True, null=True)
    url_permission = models.FileField(storage=S3StorageClass(), blank=True, null=True)
    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)

    def __str__(self):
        return f'id = {self.id}, name_article = {self.name_article}, author = {self.author}'
