"""
URL configuration for Brainer project.

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Brainer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage,name="home"),
    path('login/', views.user_login,name="user_login"),
    path('reg/', views.reg),
    path('services/', views.services),
    path('games/', views.games,name="games"),
    path('profile/', views.profile,name="user_profile"),
    path('create_profile/', views.create_user_profile,name="creating_profile"),
    path('edit/', views.edit_user_profile,name="edited_profile"),
    path('logout/',views.logoutuser,name="logout"),
    path('qs_add/',views.create_question,name="create__question"),
    #path('qs_ans/',views.answer_question,name="answer__question"),
    path('display_qs_ans/', views.display_qs_ans, name='display_qs_ans'),
    path('display_qs_ans_all/', views.display_qs_ans_all, name='display_qs_ans_all'),
    path('answer_page/', views.answer_page, name='answer_page'),
    path('calculate_score/', views.calculate_score, name='calculate_score'),
    path('score_page/<int:score>/', views.score_page, name='score_page'),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
