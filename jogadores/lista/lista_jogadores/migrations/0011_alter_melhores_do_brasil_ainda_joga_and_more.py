# Generated by Django 4.1.6 on 2023-02-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lista_jogadores", "0010_rename_gol_melhores_da_historia_info"),
    ]

    operations = [
        migrations.AlterField(
            model_name="melhores_do_brasil",
            name="ainda_joga",
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name="melhores_do_brasil", name="extras", field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="melhores_do_brasil",
            name="principal_titulo",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="melhores_do_brasil",
            name="time_principal",
            field=models.TextField(),
        ),
    ]
