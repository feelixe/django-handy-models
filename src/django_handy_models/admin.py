from django.contrib import admin
from django.conf import settings

from .models import Country, Currency, Continent, Language, Timezone

if getattr(settings, 'HANDY_MODELS_REGISTER_IN_ADMIN', False) is True:
    admin.site.register(Country)
    admin.site.register(Currency)
    admin.site.register(Continent)
    admin.site.register(Language)
    admin.site.register(Timezone)