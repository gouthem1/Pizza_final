import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django
django.setup()

from pizza.models import Pizza, Topping

pizzas = Pizza.objects.all()
toppings = Topping.objects.all()


for t in toppings:
    print("Topping ID", t.id, " ->  Topping:", t, " ->  Image Path: ", t.image_path )

for p in Pizza:
    print("Pizza ID", p.id, " ->  Pizza:", p, " ->  Image Path: ", p.image_path )
    
from django.contrib.auth.models import User
for user in User.objects.all():
    print(user.username, user.id)