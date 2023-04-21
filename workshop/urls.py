"""
URL configuration for workshop project.

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
from main import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.Main.as_view(), name="main"),
    path('room/new/', main_views.AddRoom.as_view(), name="add_room"),
    path('room/<int:room_id>/', main_views.detail_room, name="room_details"),
    path('room/delete/<int:room_id>/', main_views.delete_room, name="delete_room"),
    path('room/modify/<int:room_id>/', main_views.EditRoom.as_view(), name="edit_room"),
    path('room/reserve/<int:room_id>/', main_views.ReserveRoom.as_view(), name="reserve_room"),
    path('room/search/', main_views.search, name="search"),

]
