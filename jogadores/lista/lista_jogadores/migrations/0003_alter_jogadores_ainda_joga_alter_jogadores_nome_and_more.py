# Generated by Django 4.1.6 on 2023-02-08 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lista_jogadores", "0002_jogadores_principal_titulo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jogadores",
            name="ainda_joga",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="jogadores", name="nome", field=models.TextField(default=250),
        ),
        migrations.AlterField(
            model_name="jogadores",
            name="principal_titulo",
            field=models.TextField(default=250),
        ),
        migrations.AlterField(
            model_name="jogadores",
            name="time_principal",
            field=models.TextField(default=250),
        ),
    ]
