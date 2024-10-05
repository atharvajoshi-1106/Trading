from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('postion/', views.postion, name="postion"),
    path("order/", views.order, name='order')
]
