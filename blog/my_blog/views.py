from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

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


class allarticleapi(APIView):

    def get(self,request,format=None):
        try:
            all_ar = article.objects.all()[5:]
            data = []
            for ar in all_ar:
                data.append(
                    {
                        'title':ar.title,
                        'cover':ar.cover.url,
                        'content':ar.content,
                        'category':ar.category.title,
                        'author':ar.author.user.first_name +' '+ar.author.user.last_name,
                        'created_at':ar.created_at,
                        'poromote':ar.poromote,

                    }
                )
            return Response({'data':data},status=status.HTTP_200_OK)

        except:
            return Response({'status':'Internal server error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class contactpage(TemplateView):
    template_name = "page-contact.html"


class aboutpage(TemplateView):
    template_name = "page-about.html"

class categorypage(TemplateView):
    template_name = "category.html"
