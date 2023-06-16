from django.test import TestCase
from .models import *

product_osn = Product.objects.filter(id = id)
dop_img = dop_img_product.filter(product = product_osn)
kol = []
for i in range(1, dop_img.count()):
	kol.append(i)