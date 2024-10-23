from django.contrib import admin

# Register your models here.
from .models import Resume, PortfolioItem

admin.site.register(Resume)
admin.site.register(PortfolioItem)