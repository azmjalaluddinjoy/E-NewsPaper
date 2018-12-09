from django.contrib import admin
# from blog_post.models import Post
# erokokm lekhar proyojon nai. 
# Onno kono app er model import korte hole app_name.models
# r ek e app er model import korte hole .models import class_name dilei chole
from .models import Post
from .models import Product
from .models import Nuser
from .models import EnewsPaper
from .models import ENewsUpload, Developer, EnewsPaper02, EnewsPaper03, EnewsPaper04
from .models import tinytest, Education, Business, Sports, Entertainment, Science, LifeStyle, Comics, Cartoons, Jobs, Opinions, International,Circulation, Advertisement

# Register your models here.
admin.site.register(Post)
admin.site.register(Product)
admin.site.register(Nuser)
admin.site.register(EnewsPaper)
admin.site.register(ENewsUpload)
admin.site.register(tinytest)
admin.site.register(Education)
admin.site.register(Business)
admin.site.register(Sports)
admin.site.register(Entertainment)
admin.site.register(Science)
admin.site.register(LifeStyle)
admin.site.register(Comics)
admin.site.register(Cartoons)
admin.site.register(Jobs)
admin.site.register(Opinions)
admin.site.register(International)
admin.site.register(Circulation)
admin.site.register(Advertisement)
admin.site.register(Developer)
admin.site.register(EnewsPaper02)
admin.site.register(EnewsPaper03)
admin.site.register(EnewsPaper04)
admin.site.site_header = "The SoftTech Bangladesh E-Newspaper Administration"
admin.site.site_title = "The SoftTech Bangladesh E-Newspaper Admin Portal"
admin.site.index_title = "Welcome to The SoftTech Bangladesh Portal"