from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePage(TemplateView):
    template_name = "index.html"

class AboutPage(TemplateView):
    template_name = "about.html"

class Privacy(TemplateView):
    template_name = "privacy.html"

class Services(TemplateView):
    template_name = "services.html"

class BlogArticle(TemplateView):
    template_name = "blog-article.html"  

class CaseStudy(TemplateView):
    template_name = "case-study.html"

class Project(TemplateView):
    template_name = "projects.html"

class ServicesDetail(TemplateView):
    template_name = "services-detail.html"

class Terms(TemplateView):
    template_name = "terms.html"

class CaseStudyIndividual(TemplateView):
    template_name = "case-study-individual.html"

class Contact(TemplateView):
    template_name = "contact.html"

class Error404(TemplateView):
    template_name = "404.html"

class Team(TemplateView):
    template_name = "team.html"                                      
