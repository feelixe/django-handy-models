# Generated by Django 3.2 on 2021-05-04 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_useful_models', '0011_country_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='currency',
            new_name='currencies',
        ),
    ]
