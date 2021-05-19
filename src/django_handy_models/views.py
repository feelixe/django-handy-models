from rest_framework import viewsets

from .models import Country, Language, Continent, Currency, Timezone
from .serializers import (
    CountrySerializer,
    LanguageSerializer,
    ContinentSerializer,
    CurrencySerializer,
    TimezoneSerializer,
)

class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()

class LanguageViewSet(viewsets.ModelViewSet):
    serializer_class = LanguageSerializer
    queryset = Language.objects.all()

class ContinentViewSet(viewsets.ModelViewSet):
    serializer_class = ContinentSerializer
    queryset = Continent.objects.all()

class CurrencyViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()

class TimezoneViewSet(viewsets.ModelViewSet):
    serializer_class = TimezoneSerializer
    queryset = Timezone.objects.all()