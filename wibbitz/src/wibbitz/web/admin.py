from django.contrib import admin
from web.models import Subscribe,Customer,Feature,VideoBlog,Testimonial,MarketingFeature,Product,Blog,Contact


class CustomerAdmin(admin.ModelAdmin):
	list_display = ["id","name","image"]

admin.site.register(Customer,CustomerAdmin)


admin.site.register(Subscribe)


class FeatureAdmin(admin.ModelAdmin):
	list_display = ["id","image","icon","icon_background","title","description","testimonial_description","testimonial_author","author_desigination","testimonial_logo"]

admin.site.register(Feature,FeatureAdmin)


class VideoBlogAdmin(admin.ModelAdmin):
	list_display = ["id","title","logo","image"]

admin.site.register(VideoBlog,VideoBlogAdmin)


class TestimonialAdmin(admin.ModelAdmin):
	list_display = ["id","image","logo","description","name","desigination","company_name","is_fetutured"]

admin.site.register(Testimonial,TestimonialAdmin)


class MarketingFeatureAdmin(admin.ModelAdmin):
	list_display = ["id","title","image","description"]

admin.site.register(MarketingFeature,MarketingFeatureAdmin)


class ProductAdmin(admin.ModelAdmin):
	list_display = ["id","image","title","logo","description","color","button_color"]

admin.site.register(Product,ProductAdmin)



class BlogAdmin(admin.ModelAdmin):
	list_display = ["id","image","title","content_type","button_name"]

admin.site.register(Blog,BlogAdmin)
admin.site.register(Contact)