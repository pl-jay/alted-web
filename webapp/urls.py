from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.index, name='index'),
    path('wordprocess', views.wordprocessor_request, name='word_processor'),
    path('login', views.login, name='login_page'),
    path('home', views.upload_page, name='home_page')
]

urlpatterns += staticfiles_urlpatterns()
