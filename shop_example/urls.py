from django.urls import path
from . import views

app_name = 'shop_example'

urlpatterns = [
    path('shop/', views.MainPageView.as_view()),
    # path('shop/computers/<int:computer>', views.ComputerPageView.as_view())

]
