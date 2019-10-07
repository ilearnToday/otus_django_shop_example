from django.urls import path
from . import views

app_name = 'shop_example'

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main-page'),
    path('computers/<int:id>', views.ComputerPageView.as_view())

]
