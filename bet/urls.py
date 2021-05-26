from django.urls import path

from .views import LotView, BetView, UserView, AnimalView

app_name = "bet"


urlpatterns = [
    path('lots/', LotView.as_view()),
    path('lots/<int:pk>', LotView.as_view()),
    path('bets/', BetView.as_view()),
    path('users/', UserView.as_view()),
    path('animals/', AnimalView.as_view()),

]
