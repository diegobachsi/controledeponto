# Generated by Django 3.2.6 on 2022-07-24 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0013_auto_20220724_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='senhaprovisoria',
            name='is_active',
        ),
    ]
