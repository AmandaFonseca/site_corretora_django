# Generated by Django 3.2.7 on 2021-09-14 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210913_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('', 'Escolha uma opção'), ('F', 'Feminino'), ('M', 'Masculino')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='status_civil',
            field=models.CharField(choices=[('', 'Escolha uma opção'), ('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viúvo')], max_length=1, verbose_name='Estado civil'),
        ),
    ]