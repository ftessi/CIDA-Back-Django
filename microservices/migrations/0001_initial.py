# Generated by Django 4.2.2 on 2023-06-28 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50)),
                ('sku', models.CharField(max_length=50)),
                ('ean', models.CharField(max_length=50)),
                ('proveedor', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('marca', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('pvp', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('privileges', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('refreshtoken', models.CharField(max_length=500, unique=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]