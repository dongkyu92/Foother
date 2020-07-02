from django.urls import path
from . import views


app_name = 'maps'


urlpatterns = [
    path('create/', views.create, name='create'),
    path('<int:pk>/comment_create/', views.comment_create, name='comment_create')
]