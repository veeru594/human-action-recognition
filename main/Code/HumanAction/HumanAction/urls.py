"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from HumanAction import views as mainView
from admins import views as admins
from users import views as usr
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", mainView.index, name="index"),
    path("", mainView.index, name="index"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),

    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path('RegisterUsersView/',admins.RegisterUsersView, name='RegisterUsersView'),
    path('ActivaUsers/',admins.ActivaUsers, name='ActivaUsers'),
    path('BlockUsers/', admins.BlockUsers, name='BlockUsers'),
    path('UserActionsViewbyAdmin/', admins.UserActionsViewbyAdmin, name="UserActionsViewbyAdmin"),
    
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),
    path("UserRegisterActions/", usr.UserRegisterActions, name="UserRegisterActions"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/", usr.UserHome, name="UserHome"),
    path("UserUploadPic/", usr.UserUploadPic, name="UserUploadPic"),
    path("UploadImageAction/", usr.UploadImageAction, name="UploadImageAction"),
    path("UserStreamAction/", usr.UserStreamAction, name="UserStreamAction"),
    path("UserActionsViews/", usr.UserActionsViews, name="UserActionsViews"),
    path("UserVideoProcess/", usr.UserVideoProcess, name="UserVideoProcess"),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
