from rest_framework import routers

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'countries', views.CountryViewSet)
router.register(r'continents', views.ContinentViewSet)
router.register(r'currencies', views.CurrencyViewSet)
router.register(r'languages', views.LanguageViewSet)
router.register(r'timezones', views.TimezoneViewSet)

urlpatterns = router.urls
