from django.urls import path
from web.views import index,about


app_name = "web"


urlpatterns = [
    path("",index,name="index"),
    path("about-us/",about,name="about")
]
