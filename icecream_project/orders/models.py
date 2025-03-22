from django.contrib.auth.models import User
from django.db import models

class IceCreamFlavor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flavor = models.ForeignKey(IceCreamFlavor, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} ordered {self.quantity} of {self.flavor.name}"



