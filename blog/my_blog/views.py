from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class indexpage(TemplateView):
    
    def get(self,request,**kwargs):

        ar_data = []
        
        all_ar = article.objects.all()[:9]
        
        for ar in all_ar:
            ar_data.append({
                'title' : ar.title ,
                'cover' : ar.cover ,
                'category' : ar.category.title ,
                'article_date' : ar.created_at ,
            })
        context = {
            'ar_data' : ar_data #all of the data that related to the article
        }
        return render(request,'index.html',context)