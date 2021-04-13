from django.urls import path
from App_Login import views
urlpatterns = [
    path('', views.me,name = 'nothing')
]
