# Generated by Django 3.2.6 on 2022-07-24 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ponto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ponto',
            name='data_hora_saida',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
