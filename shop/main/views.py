from django.shortcuts import render
from .models import Catolog, Product,dop_img_product


def catalog(request):
	catolog = Catolog.objects.all()
	return render(request, "main/catalog.html",{'catolog': catolog})


def products(request,id):
	product = Product.objects.filter(id_catolog = id)
	return render(request, "main/products.html",{'product': product})


def product_car(request,ids):
	product_osn = Product.objects.get(id = ids)
	try:
		dop_img = dop_img_product.objects.filter(product=product_osn)
		kol = []
		for i in range(0, dop_img.count()):
			kol.append(i+1)
		return render(request, "main/product.html",{'product_osn': product_osn,"dop_img":dop_img,"kol":kol})
	except:
		return render(request, "main/product.html",{'product_osn': product_osn})
