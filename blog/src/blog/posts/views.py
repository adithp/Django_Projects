import datetime
import json

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from posts.forms import PostForm
from posts.models import Author,Cateagory
from main.functions import generate_form_errors



@login_required(login_url="/users/login/")
def create_post(request):
    if request.method == 'POST':
        form =PostForm(request.POST,request.FILES)
        if form.is_valid():
            tags = form.cleaned_data['categories']
            if not Author.objects.filter(user=request.user).exists():
                author = Author.objects.create(user=request.user,name=request.user.username)
            else:
                author = request.user.author
            instance = form.save(commit=False)
            instance.published_date = datetime.date.today()
            instance.author = author
            instance.save()
            tags_list = tags.split(",")
            for tag in tags_list:
               category,created = Cateagory.objects.get_or_create(title=tag.strip())
               instance.categories.add(category)
            
            response_data = {
                "title": "Succsesfully Submited",
                "message": "Succsesfully Submited",
                "status": "success",
                "redirect":"yes",
                "redirect_url":"/"
            }
        else:
            error_message = generate_form_errors(form)
            response_data = {
                "title": "Form Validation Error",
                "message": str(error_message),
                "status": "error",
                "stable":"yes"
            }
        return HttpResponse(json.dumps(response_data),content_type="application/json")
    else:
        data = {
            "title":"Testing",
            "description":"Testing",
            "short_description":"Hello Guys",
            "categories":"technoly,programming,coding",
            "time_to_read":"8 minutes"
        }
        form = PostForm(initial=data)
        context = {
            "title":"Create New Post",
            "form":form
        }
        return render(request,"posts/create.html",context=context)
