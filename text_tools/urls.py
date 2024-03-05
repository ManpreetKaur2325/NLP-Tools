"""
URL configuration for text_tools project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from toolapp import views

from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", views.login,name='login'),
    path("register/", views.register,name='register'),
    path("contact/", views.contactus,name='contact'),
    path("footer/", views.footer,name='footer'),
    path("base/" ,views.base,name='base'),
    path("allblogs/",views.allblogs,name='allblogs'),
    path("allcontentcreators/",views.allcontentcreators,name='allcontentcreators'),
    path("detailblog/<int:id>",views.detailblog, name='detailblog'),
    path("review/", views.myreview,name='review'),
    path("sidebar/",views.sidebar,name='sidebar'),
    path("changepassword/",views.changepassword,name='changepassword'),
    path("help1/",views.help,name='help1'),
    path("editprofile/",views.editprofile,name='editprofile'),
    path("myprofile/",views.myprofile,name='myprofile'),
    path("logout/",views.logout,name='logout'),
    path("forget/",views.forget,name='forget'),
]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
