from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics


from .models import *
from .serializers import *


class PlayerViewSet(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.valid(raise_exception=True)
        self.perform_update(serializer)
        return Response()

    def list(self, request, *args, **kwargs):
        serializer = PlayerSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.valid(raise_exception=True)
        self.perform_update(serializer)
        return Response()

    def list(self, request, *args, **kwargs):
        serializer = GameSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.valid(raise_exception=True)
        self.perform_update(serializer)
        return Response()

    def list(self, request, *args, **kwargs):
        serializer = BoardSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.valid(raise_exception=True)
        self.perform_update(serializer)
        return Response()

    # @extend_schema(
    #     description='Первый УРЛ',
    #     responses={
    #         200: RoomSerializer(many=True),
    #     },
    # )
    def list(self, request, *args, **kwargs):
        serializer = RoomSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

class ChanceViewSet(viewsets.ModelViewSet):
    queryset = Chance.objects.all()
    serializer_class = ChanceSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.valid(raise_exception=True)
        self.perform_update(serializer)
        return Response()

    def list(self, request, *args, **kwargs):
        serializer = ChanceSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

class PrisonViewSet(viewsets.ModelViewSet):
    queryset = Prison.objects.all()
    serializer_class = PrisonSerializer
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.valid(raise_exception=True)
        self.perform_update(serializer)
        return Response()

    def list(self, request, *args, **kwargs):
        serializer = PrisonSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

class RealtyViewSet(viewsets.ModelViewSet):
    queryset = Realty.objects.all()
    serializer_class = RealtySerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=partial)
        serializer.valid(raise_exception=True)
        self.perform_update(serializer)
        return Response()

    def list(self, request, *args, **kwargs):
        serializer = RealtySerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)

class InviteViewSet(viewsets.ModelViewSet):
    queryset = Invite.objects.all()
    serializer_class = Invite

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance=instance, data=request.data, partial=partial)
        serializer.valid(raise_exception=True)
        self.perform_update(serializer)
        return Response()

    def list(self, request, *args, **kwargs):
        serializer = InviteSerializer()
        return Response(serializer.data, status=status.HTTP_200_OK)