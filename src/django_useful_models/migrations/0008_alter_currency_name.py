# Generated by Django 3.2 on 2021-05-04 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_useful_models', '0007_auto_20210504_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
