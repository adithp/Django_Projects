from django.db import models



content_type = (
	("blog_post","Blog Post"),
	("webinar","Webinar"),
	("report","Report")
	)
COMPANY_SIZE = (
	("1","1-10"),
	("2","11-50"),
	("3","51-200"),
	("4","201-500")
	)
INDUSTRY = (
	("1","Agriculture"),
	("2","Banking & Finance"),
	("3","Business Services & Software")
	)
JOB_ROLE = (
	("1","C-Suite"),
	("2","VP")
	)
COUNTRY = (
	("us","United States"),
	("afghanistan","Afghanistan"),
	("albania","Albania")
	)

class Subscribe(models.Model):
	email = models.EmailField()

	def __str__(self):
		return self.email


class Customer(models.Model):
	name = models.CharField(max_length=150)
	image = models.FileField(upload_to="customers")
	white_image = models.FileField(upload_to="customers",blank=True,null=True)
	product = models.ForeignKey("web.Product",on_delete=models.CASCADE)

	def __str__(self):
		return self.name


class Feature(models.Model):
	image = models.ImageField(upload_to="features")
	icon = models.FileField(upload_to="features")
	icon_background = models.CharField(max_length=30)
	title = models.CharField(max_length=225)
	description = models.TextField()
	testimonial_description = models.TextField()
	testimonial_author = models.CharField(max_length=225)
	author_desigination = models.CharField(max_length=225)
	testimonial_logo = models.FileField(upload_to="features")

	class Meta:
		db_table = "web_feature"

	def __str__(self):
		return self.testimonial_author


class VideoBlog(models.Model):
	image = models.ImageField(upload_to="videoblog/image")
	title = models.CharField(max_length=128)
	logo = models.FileField(upload_to="videoblog/logo")

	class Meta:
		db_table = "web_vide_blog"
		ordering = ["-id"]

	def __str__(self):
		return self.title


class Testimonial(models.Model):
	image = models.ImageField(upload_to="testimonial/images")
	logo = models.FileField(upload_to="testimonial/logo",blank=True,null=True)
	description = models.TextField()
	name = models.CharField(max_length=128)
	desigination = models.CharField(max_length=128)
	company_name = models.CharField(max_length=128)
	is_fetutured = models.BooleanField()

	class Meta:
		db_table = "web_testimonial"
		ordering = ["-id"]

	def __str__(self):
		return self.name


class MarketingFeature(models.Model):
	image = models.FileField(upload_to="marketingfeature/")
	title = models.CharField(max_length=128)
	description = models.TextField()

	class Meta:
		db_table = "web_marketing_feature"
		ordering = ["-id"]

	def __str__(self):
		return self.title


class Product(models.Model):
	image = models.ImageField(upload_to="product/images")
	hero_image = models.ImageField(upload_to="product/hero_images")
	title = models.CharField(max_length=128)
	name = models.CharField(max_length=128)
	description = models.TextField()
	logo = models.FileField(upload_to="product/logo")
	color = models.CharField(max_length=128)
	button_color = models.CharField(max_length=128)

	class Meta:
		db_table = "web_product"
		ordering = ["-id"]

	def __str__(self):
		return self.name


class Blog(models.Model):
	image = models.ImageField(upload_to="blog")
	title = models.CharField(max_length=128)
	content_type = models.CharField(max_length=128,choices=content_type)
	button_name = models.CharField(max_length=128)

	class Meta:
		db_table = "web_blog"
		ordering = ["-id"]

	def __str__(self):
		return self.title


class Contact(models.Model):
	email = models.EmailField()
	first_name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128)
	company = models.CharField(max_length=128)
	company_size = models.CharField(max_length=128,choices=COMPANY_SIZE)
	industry = models.CharField(max_length=128,choices=INDUSTRY)
	job_role = models.CharField(max_length=128,choices=JOB_ROLE)
	country = models.CharField(max_length=128,choices=COUNTRY)
	user_agrement = models.BooleanField(default=False)

	class Meta:
		db_table = "web_contact"
		ordering = ["-id"]

	def __str__(self):
		return self.first_name