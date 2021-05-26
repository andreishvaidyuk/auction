from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Animal, Lot, Bet
from .serializers import LotSerializer, BetSerializer, UserSerializer, AnimalSerializer


class UserView(APIView):
    def get(self, request):
        """
        Метод для просмотра списка всех пользователей
        :param request:
        :return:
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"users": serializer.data})

    def post(self, request):
        """
        Метод для добавления новых пользователей
        :param request:
        :return:
        """
        user = request.data.get('users')
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({'success': "User with balance '{}' created".format(user_saved.balance)})


class AnimalView(APIView):
    def get(self, request):
        """
        Метод для получения списка имеющихся вариантов животных
        :param request:
        :return:
        """
        animals = Animal.objects.all()
        serializer = AnimalSerializer(animals, many=True)
        return Response({"animals": serializer.data})

    def post(self, request):
        """
        Метод ля добавления животных, на которых потом будут выставляться лоты
        :param request:
        :return:
        """
        animal = request.data.get('animals')
        serializer = AnimalSerializer(data=animal)
        if serializer.is_valid(raise_exception=True):
            animal_saved = serializer.save()
        return Response({'success': "Animal '{}' created".format(animal_saved.type)})


class LotView(APIView):
    def get(self, request, pk=None):
        """
        Метод для получения списка лотов.
        Если в запросе передан номер лота, то выводится этот лот и все ставки на него.
        Иначе выводится просто список всех лотов.
        :param request:
        :param pk: Lot id
        :return:
        """
        if pk:
            lots = generics.get_object_or_404(Lot.objects.all(), pk=pk)
            lot_serializer = LotSerializer(lots)
            bets = Bet.objects.filter(lot=pk)
            bet_serializer = BetSerializer(bets, many=True)
            return Response([{"lots": lot_serializer.data, "bets": bet_serializer.data}])
        else:
            lots = Lot.objects.all()
            lot_serializer = LotSerializer(lots, many=True)
            return Response({"lots": lot_serializer.data})

    def post(self, request):
        """
        Метод для создания лота
        :param request:
        :return:
        """
        lot = request.data.get('lots')
        serializer = LotSerializer(data=lot)
        if serializer.is_valid(raise_exception=True):
            lot_saved = serializer.save()
        return Response({'success': "Lot '{}' created".format(lot_saved.animal.type)})


class BetView(APIView):
    def get(self, request):
        """
        Метод для получения всего списка ставок
        :param request:
        :return:
        """
        bets = Bet.objects.all()
        serializer = BetSerializer(bets, many=True)
        return Response({'bets': serializer.data})

    def post(self, request):
        """
        Метод выставления ставки на лот
        :param request:
        :return:
        """
        bet = request.data.get('bets')
        serializer = BetSerializer(data=bet)
        if serializer.is_valid(raise_exception=True):
            bet_saved = serializer.save()
        return Response({'success': "Bet with rate '{}' created".format(bet_saved.rate)})
