from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    bio = models.TextField(verbose_name='بیوگرافی')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=15,verbose_name='تلفن')

    class Meta:
        verbose_name = 'رزومه'
        verbose_name_plural = 'رزومه'
    def __str__(self):
        return self.name

class PortfolioItem(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    description = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True, verbose_name='تصویر')
    link = models.URLField(blank=True)

    class Meta:
        verbose_name = 'نمونه  کار'
        verbose_name_plural = 'نمونه کارها'

    def __str__(self):
        return self.title
