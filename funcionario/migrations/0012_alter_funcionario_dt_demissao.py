# Generated by Django 3.2.6 on 2022-07-23 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0011_alter_funcionario_dt_demissao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='dt_demissao',
            field=models.DateField(blank=True, null=True),
        ),
    ]