# Generated by Django 2.1.5 on 2019-04-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=123456, max_length=30, unique=True, verbose_name='Nome de Usuário'),
            preserve_default=False,
        ),
    ]
