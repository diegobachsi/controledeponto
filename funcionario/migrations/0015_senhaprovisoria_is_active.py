# Generated by Django 3.2.6 on 2022-07-24 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0014_remove_senhaprovisoria_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='senhaprovisoria',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Ativa'),
        ),
    ]