# Generated by Django 3.2.6 on 2022-07-17 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0007_auto_20220717_1818'),
        ('supervisor', '0005_supervisor_funci'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisor',
            name='funci',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionario.funcionario'),
        ),
    ]
