# Generated by Django 2.1.2 on 2018-12-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hethong', '0004_auto_20181220_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container_product_detail',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='container_product_log',
            name='expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='container_product_log',
            name='manufacturing_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
