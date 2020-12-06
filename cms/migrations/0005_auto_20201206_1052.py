# Generated by Django 3.1.4 on 2020-12-06 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0004_auto_20201206_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='finish_flag',
            field=models.BooleanField(default=0, verbose_name='マッチング判定'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='shop_ID',
            field=models.CharField(blank=True, max_length=40, verbose_name='店舗名'),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='shop_ID',
            field=models.CharField(max_length=40, verbose_name='店舗名'),
        ),
    ]
