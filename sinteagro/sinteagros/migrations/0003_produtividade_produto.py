# Generated by Django 2.1.5 on 2019-02-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sinteagros', '0002_auto_20190206_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtividade',
            name='produto',
            field=models.CharField(default='Milho', max_length=10),
            preserve_default=False,
        ),
    ]
