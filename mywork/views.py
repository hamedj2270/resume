from django.shortcuts import render
from .models import Resume, PortfolioItem
from django.utils.translation import gettext as _

def home(request):
    resume = Resume.objects.first()
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'portfolio/home.html', {'resume': resume, 'portfolio_items': portfolio_items})


