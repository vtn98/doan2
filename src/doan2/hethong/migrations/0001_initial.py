# Generated by Django 2.1.2 on 2018-12-17 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('dele', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='container_product_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField()),
                ('container_id', models.PositiveIntegerField()),
                ('provider_id', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('manufacturing_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='container_product_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('container_from', models.PositiveIntegerField()),
                ('container_to', models.PositiveIntegerField()),
                ('product_id', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('manufacturing_date', models.DateField()),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('user_id', models.PositiveIntegerField()),
                ('price_total', models.PositiveIntegerField(blank=True, null=True)),
                ('order_date', models.DateField(auto_now_add=True)),
                ('export_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='order_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.PositiveIntegerField()),
                ('product_id', models.PositiveIntegerField()),
                ('amount', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('manufacturing_date', models.DateField()),
                ('expiry_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('dele', models.PositiveSmallIntegerField()),
                ('product_type', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='provider_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('product_id', models.PositiveIntegerField()),
                ('dele', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('code', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('status', models.PositiveSmallIntegerField()),
                ('account_type', models.CharField(max_length=45)),
                ('dele', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
