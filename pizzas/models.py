from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pizza(models.Model):
    text = models.CharField(max_length=200)
    image = models.ImageField(upload_to="pizzas", default='cheese_pizza.png')

    def __str__(self):
        return self.text

class Topping(models.Model):
    text = models.CharField(max_length=200)
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'toppings'


    def __str__(self):
        return self.text

class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}..."