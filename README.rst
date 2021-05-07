django-handy-models
===================

A Django App that adds pre-populated models for common use cases.
Includes models for **Continents**, **Countries**, **Language**,
**Currencies**, **Timezones**.

Example data
============

::

    {
        "name_exonym": "Sweden",
        "name_endonym": "Sverige",
        "iso_3166_1_alpha_2": "SE",
        "capital_exonym": "Stockholm",
        "capital_endonym": "Stockholm",
        "calling_code": "46",
        "continent": {
            "name": "Europe",
            "abbreviation": "EU"
        },
        "languages":[
            {
                "name_exonym": "Swedish",
                "name_endonym": "Svenska",
                "iso_639_1": "sv"
            }
        ],
        "currencies":[
            {
                "name": "Swedish Krona",
                "name_plural": "Swedish kronor",
                "symbol_exonym": "Skr",
                "symbol_endonym": "kr",
                "iso_4217": "SEK"
            }
        ]
    }

Setup
=====

Install from pip

::

    pip install django-handy-models

add to INSTALLED\_APPS in Django project's settings.py

::

    INSTALLED_APPS = [
        ...
        'django_handy_models',
    ]

Migrate database

::

    python manage.py migrate

Load data from fixtures

::

    python manage.py loaddata django_handy_models

