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

        pr_data = []
        all_promotions = article.objects.filter(poromote=True)
        for pr_ar in all_promotions:
            pr_data.append({
                'title' : pr_ar.title,
                "category" : pr_ar.category.title,
                'author' : pr_ar.author.user.first_name,
                'cover' : pr_ar.cover                
            })
        
        
        
        
        

        context = {
            'ar_data' : ar_data    ,
            'poromote_data' : pr_data                  #all of the data that related to the article
        }
        return render(request,'index.html',context)


class contactpage(TemplateView):
    template_name = "page-contact.html"


class aboutpage(TemplateView):
    template_name = "page-about.html"