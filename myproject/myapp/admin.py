from django.contrib import admin
from myapp.models import  Product, Profile, Purchase, Review
# from myapp.models import Category, Product, Profile, Purchase, Review


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['namecategory', 'slug']
#     prepopulated_fields = {'slug': ('namecategory',)}

# admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['seller','name', 'picture', 'price', 'color', 'size', 'quantity']
    # list_display=['seller','name', 'picture', 'category', 'slug', 'price', 'color', 'size', 'quantity']
    # prepopulated_fields = {'slug': ('name',)}
    
admin.site.register(Product,ProductAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display=['user', 'Firstname','Lastname', 'email', 'DOB', 'address', 'city', 'country', 'zipcode', 'tel']
    list_editable = ['address', 'city', 'country', 'zipcode']

admin.site.register(Profile,ProfileAdmin)

class PurchaseAdmin(admin.ModelAdmin):
    list_display=['profile', 'product','quantity', 'coupon', 'payment' ]
    list_editable = ['product', 'quantity']

admin.site.register(Purchase,PurchaseAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display=['product', 'profile','ratings', 'comment',]

admin.site.register(Review,ReviewAdmin)

