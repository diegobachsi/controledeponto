# Generated by Django 3.2.6 on 2022-07-24 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ponto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricula', models.CharField(max_length=10)),
                ('data_hora_entrada', models.DateTimeField()),
                ('data_hora_saida', models.DateTimeField()),
            ],
        ),
    ]
