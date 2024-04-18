import json
from django.http.response import HttpResponse 
from django.shortcuts import render,get_object_or_404
from web.models import Subscribe,Customer,Feature,VideoBlog,Testimonial,MarketingFeature,Product,Blog,Contact
from web.forms import ContactForm

def index(request):
	customers = Customer.objects.all()
	latest_customers = Customer.objects.all()[:4]
	features = Feature.objects.all()
	videoblogs = VideoBlog.objects.all()[:3]
	testimonials_featured = Testimonial.objects.filter(is_fetutured=True)
	marketing_features = MarketingFeature.objects.all()
	products = Product.objects.all()
	blogs = Blog.objects.all()
	form = ContactForm()
	context = {
	"customers":customers,
	"features":features,
	"videoblogs":videoblogs,
	"testimonials_featured":testimonials_featured,
	"marketing_features":marketing_features,
	"products":products,
	"blogs":blogs,
	"form":form,
	"latest_customers":latest_customers,
	}
	return render(request,"index.html",context=context)


def subscribe(request):
	email = request.POST.get("email")
	if not Subscribe.objects.filter(email=email).exists():
		Subscribe.objects.create(
			email = email
			)
		response_data = {
		"status":"success",
		"message":"You Successfully Subscribed",
		"title":"Successfully Registerd"
		}
	else:
		response_data = {
		"status":"error",
		"message":"You Have Already Subscribed",
		"title":"Already Registerd"
		}

	return HttpResponse(json.dumps(response_data),content_type="application/javascript")


def contact(request):
	form = ContactForm(request.POST)
	if form.is_valid():
		form.save()
		response_data = {
		"status":"success",
		"message":"You Successfully Subscribed",
		"title":"Successfully Registerd"
		}
	else:
		response_data = {
		"status":"error",
		"message":"You Have Already Subscribed",
		"title":"Already Registerd"
		}

	return HttpResponse(json.dumps(response_data),content_type="application/javascript")

	
def product(request,pk):
	product = get_object_or_404(Product.objects.filter(pk=pk))
	customers = Customer.objects.filter(product=product)
	context = {
		"product":product,
		"customers":customers
	}
	return render(request,"product.html",context=context)



