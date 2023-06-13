"""
URL configuration for mywebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.forms, name='html'),

    path('',views.index, name='index'),

    path('data/',views.data, name='data'),






]

'''so what is happening here that in views file i will create  varios veiws  or like pages for my website and define the 
function for them  so in the url file i will have to specify the path for the view , it takes three arguments 
1: a sting value that tells what is to be appended at the end of the url so here i have created a view called as 
about and when i append the view about at the end of the url of my server like http://127.0.0.1:8000/about
it will take me to the about view, and the third argument that it takes is the name that must be equal to that of the 
view, 
the second argument view.    is the argument that specifies the function that will run ie we have to define this function in 
views'''
