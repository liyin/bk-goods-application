# Generated by Django 2.2.6 on 2022-01-23 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good_purchase', '0003_auto_20220120_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupapply',
            name='status',
            field=models.IntegerField(choices=[(1, '已退回'), (2, '在使用'), (3, '退回中'), (4, '购买中'), (5, '待收货')], verbose_name='物资状态'),
        ),
    ]
