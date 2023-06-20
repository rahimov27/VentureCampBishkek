from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name ='about'),
    path('blog', views.blog, name = 'blog'),
    path('project', views.project, name = 'project'),
    path('service', views.service, name = 'service'),
    path('single', views.single, name = 'single'),

]
