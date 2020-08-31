from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_webdevs, name='webdevs'),
    path('<webdev_id>', views.webdev_detail, name='webdev_detail'),
]
