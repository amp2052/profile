from django.contrib.sitemaps.views import sitemap
from app.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skills/', views.skills, name='skills'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('education/', views.education, name='education'),
]
