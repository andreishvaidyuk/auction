from rest_framework import serializers

from .models import User, Animal, Lot, Bet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'balance')

    def create(self, data):
        return User.objects.create(**data)


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ('type', 'breed', 'name', 'owner')

    def create(self, data):
        return Animal.objects.create(**data)


class LotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lot
        fields = ('id', 'animal', 'price', 'owner')

    def create(self, data):
        return Lot.objects.create(**data)


class BetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bet
        fields = ('id', 'lot', 'rate', 'owner')

    def create(self, data):
        return Bet.objects.create(**data)

