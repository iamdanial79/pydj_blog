from django.conf.urls import url,include
from django.urls.conf import path
from . import views

urlpatterns = [
    url(r'^$',views.indexpage.as_view(),name='index'),
    url (r'^contact/$',views.contactpage.as_view(),name='contact'),
    url (r'^about/$',views.aboutpage.as_view(),name='about'),
    url (r'^category/$',views.aboutpage.as_view(),name='category'),


    url(r'^article/all/$',views.allarticleapi.as_view(),name='all_article'),

]