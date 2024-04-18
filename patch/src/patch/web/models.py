from django.db import models



FAQ_TYPE = (
	("rent_tracking","Rent Tracking"),
	("new_deposit","New Deposit"),
	("existing_deposit","Existing Deposit"),
	)



class Testimonial(models.Model):
	name = models.CharField(max_length=225)
	designation = models.CharField(max_length=225,default="Software Enginer")
	description = models.TextField(blank=True,null=True)
	image = models.ImageField(upload_to="testimonial/")

	def __str__ (self):
		return self.name

		
class Promoter(models.Model):
	name = models.CharField(max_length=225)
	image = models.ImageField(upload_to="promoters/")

	def __str__(self):
		return self.name

		
class Faq(models.Model):
	title = models.CharField(max_length=225)
	description = models.TextField()
	faq_type = models.CharField(max_length=125,choices=FAQ_TYPE)

	def __str__(self):
		return self.title

class Subscribe(models.Model):
	email = models.EmailField()


	def __str__(self):
		return self.email