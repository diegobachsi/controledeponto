# Generated by Django 3.2.6 on 2022-07-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0008_auto_20220717_2217'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='dt_demissao',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='funcionario',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='dt_admissao',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='dt_nascimento',
            field=models.CharField(max_length=100),
        ),
    ]
