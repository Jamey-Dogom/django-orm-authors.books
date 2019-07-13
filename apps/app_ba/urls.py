from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book', views.add_book),
    url(r'^authors', views.authors),
    url(r'^add_author', views.add_author),
    url(r'^view_author/', views.display_author),
]