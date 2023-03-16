"""banterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from banterclone import views

urlpatterns = [
    path("", views.HomePage.as_view(), name="home"),
    path("about/", views.AboutPage.as_view(), name="about"),
    path("privacy/", views.Privacy.as_view(), name="privacy"),
    path("services/", views.Services.as_view(), name="services"),
    path("blog/", views.BlogArticle.as_view(), name="blog"),
    path("casestudy/", views.CaseStudy.as_view(), name="casestudy"),
    path("projects/", views.Projects.as_view(), name="projects"),
    path("services-detail/", views.ServicesDetail.as_view(), name="services-detail"),
    path("terms/", views.Terms.as_view(), name="terms"),
    path("casestudyindividual", views.CaseStudyIndividual.as_view(), name="case-study-individual"),
    path("contact/", views.Contact.as_view(), name="contact"),
    path("404", views.Error404.as_view(), name="404"),    
    path('admin/', admin.site.urls),
]
