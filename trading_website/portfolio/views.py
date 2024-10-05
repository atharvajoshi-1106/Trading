from django.shortcuts import render
from .models import Investment

def home(request):
    return render(request, 'portfolio/home.html')

def portfolio(request):
    investments = Investment.objects.all()
    total_investment = sum([i.amount_invested for i in investments])
    total_profit_loss = sum([i.profit_loss for i in investments])
    return render(request, 'portfolio/portfolio.html', {
        'investments': investments,
        'total_investment': total_investment,
        'total_profit_loss': total_profit_loss
    })

def postion(request):
    return render(request,'portfolio/postion.html')

def order(request):
    return render(request,'portfolio/order.html')


# Create your views here.
