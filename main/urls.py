from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('create', create, name='create'),
    path('edit/<int:pk>', edit, name='edit'),
    path('delete/<int:pk>', delete, name='delete')
]
