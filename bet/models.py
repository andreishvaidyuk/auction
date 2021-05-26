from django.db import models


# User model
class User(models.Model):
    balance = models.FloatField()

    def __str__(self):
        return str(self.balance)


# Animal model (for Kitty or Hedgehog)
class Animal(models.Model):
    type = models.CharField(max_length=10)
    breed = models.CharField(max_length=20)
    name = models.CharField(max_length=15)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Lot model
class Lot(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    price = models.FloatField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.animal.name


# Bet model
class Bet(models.Model):
    rate = models.FloatField()
    lot = models.ForeignKey(Lot, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rate