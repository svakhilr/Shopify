from django.urls import path
from .import views
urlpatterns = [
    path('', views.home , name='home'),
    path('quickview/',views.quick_view,name='quickview'),
    path('errorpage/',views.errorpage,name='errorpage')
    

]