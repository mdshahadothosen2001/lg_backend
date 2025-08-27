from django.urls import path

from engage.accounts.views import LoginView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
