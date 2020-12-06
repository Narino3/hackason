# Generated by Django 3.1.4 on 2020-12-06 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20201206_0300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='person_type',
        ),
        migrations.AddField(
            model_name='entry',
            name='person_type',
            field=models.ManyToManyField(blank=True, to='cms.PType'),
        ),
        migrations.AlterField(
            model_name='entry',
            name='shop_ID',
            field=models.CharField(blank=True, max_length=40, verbose_name='店舗ID'),
        ),
        migrations.AlterField(
            model_name='recruit',
            name='shop_ID',
            field=models.IntegerField(max_length=40, verbose_name='店舗ID'),
        ),
    ]
