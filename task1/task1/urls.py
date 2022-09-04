"""task1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from task_app import views
from task_app.views import GetAllPosts

urlpatterns = [
    path("admin/", admin.site.urls),
    path("createpost/", views.createpost, name="create_post"),
    path("createbook/", views.createbook, name="create_book"),
    # path("", views.get_all_posts, name="show_post"),
    path("", GetAllPosts.as_view(), name="show_post"),

    path("showbirds", views.get_all_birds, name="show_birds"),

    path("login/", views.LoginUser.as_view(), name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.RegisterUser.as_view(), name="register")

]
