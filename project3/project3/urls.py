"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from project3app import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
        path('',views.index,name="index_view"),

        path('first',views.first),
        path('second',views.temp2,name="view2"),
        path('third',views.temp3,name="view3"),
        path('fourth',views.temp4,name="view4"),
        path('fifth',views.temp5,name="view5"),
        path('sixt',views.temp6,name="view6"),
        path('sevent',views.temp7,name="view7"),
        path('eigth',views.temp8,name="view8"),
        path('nine',views.temp9,name="view9"),
        path('ten',views.temp10,name="view10"),
]
