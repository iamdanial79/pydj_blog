from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.indexpage.as_view(),name='index')


]