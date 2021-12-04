from django.conf.urls import url,include
from django.urls.conf import path
from django.views.generic.base import View
from . import views

urlpatterns = [
    url(r'^$',views.indexpage.as_view(),name='index'),
    url (r'^contact/$',views.contactpage.as_view(),name='contact'),
    url (r'^about/$',views.aboutpage.as_view(),name='about'),
    url (r'^category/$',views.aboutpage.as_view(),name='category'),


    url(r'^article/$',views.singlearticleapi.as_view(),name='single_article'),
    url(r'^article/all/$',views.allarticleapi.as_view(),name='all_article'),
    url(r'^article/search/$',views.SearchArticleApi.as_view(),name='search_article'),

]