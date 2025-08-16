from ..models import Product, Transaction


p = Product.objects.get(id=1)

p.order_product(2).save()