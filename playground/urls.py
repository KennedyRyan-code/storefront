from django.urls import path
from . import views

#URLconf for the playground app
urlpatterns = [
    path('index/', views.index, name='index'),
]