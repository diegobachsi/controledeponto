# Generated by Django 3.2.6 on 2022-07-17 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setor', '0001_initial'),
        ('funcionario', '0006_funcionario_id_supervisor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='id_supervisor',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='id_setor',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='setor.setor'),
            preserve_default=False,
        ),
    ]
