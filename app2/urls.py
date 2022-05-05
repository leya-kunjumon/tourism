"""pro2 URL Configuration

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
from app2 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('homee/',views.homee),
    path('signup/',views.signup),
    path('sign/',views.sign),
    path('regi/',views.register),
    path('home1/',views.home1),
    path('signup1/',views.signup1),
    path('sign1/',views.sign1),
    path('login/',views.login),
    path('reg/',views.reg),
    path('home3/',views.home3),
    path('signup3/',views.signup3),
    path('sign3/',views.sign3),
    path('home4/',views.home4),
    path('signup4/',views.signup4),
    path('sign4/',views.sign4),
    path('tvm/<int:id>',views.tvm),
    path('alpi/<int:id>',views.alpi),
    path('klm/<int:id>',views.klm),
    path('erkm/<int:id>',views.erkm),
    path('idki/<int:id>',views.idki),
    path('trsr/<int:id>',views.trsr),
    path('kzkod/<int:id>',views.kzkod),
    path('ksrgd/<int:id>',views.ksrgd),
    path('home5/',views.home5),
    path('signup5/',views.signup5),
    path('sign5/',views.sign5),
    path('explore1/<int:id>',views.explore1),
    path('home6/',views.home6),
    path('signup6/',views.signup6),
    path('sign6/',views.sign6),
    path('explore2/<int:id>',views.explore2),
    path('home7/',views.home7),
    path('signup7/',views.signup7),
    path('sign7/',views.sign7),
    path('explore3/<int:id>',views.explore3),
    path('home8/',views.home8),
    path('signup8/',views.signup8),
    path('sign8/',views.sign8),
    path('explore4/<int:id>',views.explore4),
    path('home9/',views.home9),
    path('signup9/',views.signup9),
    path('sign9/',views.sign9),
    path('explore5/<int:id>',views.explore5),
    path('home10/',views.home10),
    path('signup10/',views.signup10),
    path('sign10/',views.sign10),
    path('explore6/<int:id>',views.explore6),
    path('home11/',views.home11),
    path('signup11/',views.signup11),
    path('sign11/',views.sign11),
    path('explore7/<int:id>',views.explore7),
     path('home12/',views.home11),
    path('signup12/',views.signup11),
    path('sign12/',views.sign11),
    path('explore8/<int:id>',views.explore8),
    path('profile/<int:id>',views.profile),
    path('orgin/',views.orgin),
    path('del/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('orgin1/',views.orgin1),
    path('update/<int:id>',views.update),
    
    
    
    
    
    
    
    
    
    
    
    
]
