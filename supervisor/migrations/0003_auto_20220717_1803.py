# Generated by Django 3.2.6 on 2022-07-17 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0005_remove_funcionario_id_supervisor'),
        ('supervisor', '0002_supervisor_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supervisor',
            name='nome',
        ),
        migrations.AddField(
            model_name='supervisor',
            name='matricula',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionario.funcionario'),
        ),
    ]
