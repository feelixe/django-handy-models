from rest_framework import serializers
from .models import Continent, Country, Currency, Timezone, Language

class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = '__all__'

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class TimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timezone
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    continent = ContinentSerializer()
    languages = LanguageSerializer(many=True)
    currencies = CurrencySerializer(many=True)

    class Meta:
        model = Country
        fields = '__all__'