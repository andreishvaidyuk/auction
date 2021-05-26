from django.contrib import admin

from .models import Lot, User, Animal, Bet

admin.site.register(Lot)
admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Bet)

