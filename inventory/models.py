from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def order_product(self, quantity):
        if quantity > self.stock:
            raise ValueError("Insufficient stock")
        self.stock -= quantity

        transaction = Transaction.objects.create(
            product=self,
            quantity=quantity,
            total_price=self.price * quantity,
            type="sale",
        )

        return self

    def commit(self):
        self.save()


class Transaction(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=10, choices=[("sale", "Sale"), ("purchase", "Purchase")]
    )
