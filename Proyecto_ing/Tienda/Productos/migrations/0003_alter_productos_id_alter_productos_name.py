# Generated by Django 4.1.1 on 2022-12-19 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_productos_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID_producto'),
        ),
        migrations.AlterField(
            model_name='productos',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre_Producto'),
        ),
    ]