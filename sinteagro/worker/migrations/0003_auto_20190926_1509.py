# Generated by Django 2.1.5 on 2019-09-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worker', '0002_auto_20190916_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='cpf',
            field=models.CharField(max_length=14, primary_key=True, serialize=False, unique=True),
        ),
    ]