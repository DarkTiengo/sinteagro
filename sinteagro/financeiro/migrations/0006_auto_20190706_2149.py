# Generated by Django 2.1.5 on 2019-07-07 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0005_auto_20190629_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrato',
            name='document',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AddField(
            model_name='extrato',
            name='type',
            field=models.CharField(default='null', max_length=10),
        ),
    ]