from django.urls import path
from . import views

app_name = 'shop_example'

urlpatterns = [
    path('', views.MainPageView.as_view()),
    # path('computers/<int:computer>', views.ComputerPageView.as_view())

]
