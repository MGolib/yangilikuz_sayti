from django.db import models

# Create your models here.

class Yangiliklar(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'news'

class Info(models.Model):
    title = models.CharField(max_length=100)
    info = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'info'
        verbose_name_plural = 'Infos'

class Dunyo(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'foreignnews'

class Texnologiya(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'texnologiyalar'

class yangilikuz(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'yangiliklaruz'
