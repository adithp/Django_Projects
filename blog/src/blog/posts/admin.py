from django.contrib import admin
from posts.models import Author,Cateagory,Post


class AutherAdmin(admin.ModelAdmin):
    list_display = ("name","title")
    
admin.site.register(Author)

admin.site.register(Cateagory)

class PostAdmin(admin.ModelAdmin):
    list_display = ("title","auther","published_date","short_description")
    
admin.site.register(Post)