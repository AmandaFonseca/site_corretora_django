# Generated by Django 3.2.7 on 2021-09-07 05:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('cpf', models.CharField(max_length=11, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=150)),
                ('sexo', models.CharField(choices=[('F', 'Feminino'), ('M', 'Masculino')], max_length=1)),
                ('telefone', models.CharField(max_length=18, validators=[django.core.validators.RegexValidator(message="O número de telefone deve ser inserido no formato: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('endereco', models.CharField(max_length=250)),
                ('data_nascimento', models.DateField()),
                ('status_civil', models.CharField(choices=[('S', 'Solteiro'), ('C', 'Casado'), ('D', 'Divorciado'), ('V', 'Viúvo')], max_length=1, verbose_name='Estado civil')),
                ('salario', models.CharField(max_length=20)),
            ],
        ),
    ]
