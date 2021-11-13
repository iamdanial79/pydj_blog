from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from ckeditor.fields import RichTextField
from datetime import datetime

#add user field
class userprofile(models.Model):
    user = models.OneToOneField( User,on_delete=models.CASCADE )
    avatar = models.ImageField( upload_to="files/user_avatar/", null=True , blank=True )
    description = models.CharField(max_length=5000)

#add article field
class article(models.Model):
    title = models.CharField( max_length=200 , null=False , blank=False )
    cover = models.ImageField( upload_to='files/article_cover/' , null=False , blank=False )
    content = RichTextField()
    created_at = models.DateTimeField(default=datetime.now , blank=False)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    author = models.OneToOneField(userprofile, on_delete=models.CASCADE)



class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    cover = models.ImageField(upload_to='files/category_cover/' )
    def __str__(self):
        return self.title
