from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.indexpage.as_view(),name='index'),
    url (r'^contact/$',views.contactpage.as_view(),name='contact'),
    url (r'^about/$',views.aboutpage.as_view(),name='about')


]