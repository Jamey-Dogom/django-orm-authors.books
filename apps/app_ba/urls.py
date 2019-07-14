from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_book', views.add_book),
    url(r'^authors', views.authors),
    url(r'^add_author', views.add_author),
     url(r'^view_author/(?P<author_id>[0-9]+)/', views.display_author),
     url(r'^view_book/(?P<author_id>[0-9]+)/', views.display_author),
     url(r'^append_book_to_author/(?P<author_id>[0-9]+)', views.append_book),
     url(r'^append_author_to_book/(?P<author_id>[0-9]+)', views.append_book),
]