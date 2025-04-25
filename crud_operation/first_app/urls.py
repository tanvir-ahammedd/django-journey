from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('data/', views.data, name='datapage'),
    path('delete/<int:roll>', views.delete, name='delete_data')
]
