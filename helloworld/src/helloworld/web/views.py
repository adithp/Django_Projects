from django.shortcuts import render
from django.http.response import HttpResponse


def index(request):
	name = "Adith P"
	age = 18
	context = {
		"name":name,
		"age":age
	}
	return render(request,"index.html",context=context)


def about(request):
	return render(request,"about.html")