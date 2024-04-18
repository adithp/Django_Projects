import json


from django.shortcuts import render , redirect
from django.urls import reverse
from django.http.response import HttpResponse


from web.models import Testimonial ,Promoter ,Faq,Subscribe


def index(request):
	testimonials = Testimonial.objects.all()
	promoters = Promoter.objects.all()
	rt_faqs = Faq.objects.filter(faq_type="rent_tracking")
	nd_faqs = Faq.objects.filter(faq_type="new_deposit")
	ed_faqs = Faq.objects.filter(faq_type="existing_deposit")

	context = {
	"testimonials":testimonials,
	"promoters":promoters,
	"rt_faqs" : rt_faqs,
	"nd_faqs" : nd_faqs,
	"ed_faqs" : ed_faqs
	}
	return render(request,"index.html", context=context)


def subscribe(request):
	email = request.POST.get("email")
	if not Subscribe.objects.filter(email=email).exists():
		Subscribe.objects.create(
			email = email
			)
		response_data = {
			"status":"success",
			"message": "You Successfully Subscribed Newsletter",
			"title" : "Successfully Registerd"
		}
	else:
		response_data = {
			"status":"error",
			"message": "You Already Subscribed Newsletter",
			"title" : "Already Registerd"
		}

	return HttpResponse(json.dumps(response_data),content_type="application/javascript")