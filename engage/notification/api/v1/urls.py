from django.urls import path

from engage.notification.api.v1.views import NoticeListView, EvenListView


urlpatterns = [
    path('list/', NoticeListView.as_view(), name='notice_list'),
    path('even/', EvenListView.as_view(), name='even_list'),
]
