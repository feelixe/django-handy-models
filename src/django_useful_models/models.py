from django.db import models
from django.core.validators import RegexValidator

class Continent(models.Model):
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=2, unique=True)

    class Meta:
        verbose_name_plural = 'continents'

    def __str__(self):
        return self.name

class Currency(models.Model):
    name = models.CharField(max_length=255, null=True) # remove null=True, after inserting data + add unique
    name_plural = models.CharField(max_length=255, null=True) # remove null=True,
    symbol_exonym = models.CharField(max_length=100, null=True)
    symbol_endonym = models.CharField(max_length=100, null=True)
    iso_4217 = models.CharField(max_length=10, null=True, blank=True, unique=True)
    # abbre name and fraction

    class Meta:
        verbose_name_plural = 'currencies'

    def __str__(self):
        return self.name or self.iso_4217

class Language(models.Model):
    name_exonym = models.CharField(max_length=255, null=True)   # remove null=True, after inserting data + add unique
    name_endonym = models.CharField(max_length=255, null=True)
    iso_639_1 = models.CharField(max_length=2, null=True, unique=True)

    def __str__(self):
        return self.name_exonym or self.iso_639_1

class Timezone(models.Model):
    name = models.CharField(max_length=100)
    utc_offset = models.DurationField()
    utc_dst_offset = models.DurationField(help_text='Daylight saving offset', null=True)

class Country(models.Model):
    name_exonym = models.CharField(max_length=255, unique=True)
    name_endonym = models.CharField(max_length=255)
    iso_3166_1_alpha_2 = models.CharField(
        max_length=2,
        null=True, #remove later
        validators=[
            RegexValidator(
                regex=r'^[A-Z]{2}$',
                message='Exactly two uppercase letters required.'
            )
        ]
    )
    capital_exonym = models.CharField(max_length=255, null=True)
    capital_endonym = models.CharField(max_length=255, null=True)
    calling_code = models.CharField(max_length=20)
    continent = models.ForeignKey(Continent, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)
    currencies = models.ManyToManyField(Currency)

    class Meta:
        verbose_name_plural = 'countries'

    def __str__(self):
        return self.name_exonym