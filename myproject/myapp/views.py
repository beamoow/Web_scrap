from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Profile, Product
# from myapp.models import Profile, Product, Category
from myapp.forms import ProfileForm, NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 

from django.views.generic import ListView

# from django.core.paginator import Paginator, EmptyPage, InvalidPage


# def ItemListView(request):
#     model = Product
#     paginate_by = Paginator(model, 3)
#     try:
#         page=int(request.GET.get('page','1'))
#     except:
#         page=1
#     try:
#         productperPage=model.page(page)
#     except (EmptyPage,InvalidPage):
#         productperPage=model.page(model.num_pages)

#     return render(request,'home.html',{'model':productperPage,'category':paginate_by})




# class ItemListView(ListView):
#     model = Product
#     template_name = 'home.html'


class ItemListView(ListView):
    model = Product
    template_name = 'home.html'





# def categories(request):
#     return {
#         'categories': Category.objects.all()
#     }


# def all_products(request):
#     products = Product.products.all()
#     return render(request, 'home.html', {'products': products})


# def category_list(request, category_slug=None):
#     category = get_object_or_404(Category, slug=category_slug)
#     products = Product.objects.filter(category=category)
#     return render(request, 'category.html', {'category': category, 'products': products})


# def product_detail(request, slug):
#     product = get_object_or_404(Product, slug=slug, in_stock=True)
#     return render(request, 'item.html', {'product': product})

# def item(request):
#     return render(request, 'item.html') 

# def productPage(request,category_slug,product_slug):
#     try:
#         product=Product.objects.get(category__slug=category_slug,slug=product_slug)
#     except Exception as e :
#         raise e
#     return render(request,'product.html',{'product':product})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("home")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("home")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("home")


def profile(request): 
    instance = get_object_or_404(Profile, user=request.user)
    form = ProfileForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        context = {
            'form':form,
            'user':request.user
            }
        return render(request, 'profile.html', context) 




