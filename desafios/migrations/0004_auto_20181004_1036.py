# Generated by Django 2.1.1 on 2018-10-04 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafios', '0003_academico_cgu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pergunta',
            name='alternativa_certa',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=2),
        ),
    ]
