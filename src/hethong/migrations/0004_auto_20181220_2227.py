# Generated by Django 2.1.2 on 2018-12-20 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hethong', '0003_auto_20181220_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_detail',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='order_detail',
            name='manufacturing_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]