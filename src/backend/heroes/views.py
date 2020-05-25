from .models import Hero
from .serializers import HeroSerializer
from rest_framework import generics


class HeroListCreate(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
