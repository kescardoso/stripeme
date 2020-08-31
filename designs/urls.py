from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_designs, name='designs'),
    path('<design_id>', views.design_detail, name='design_detail'),
]
