# Generated by Django 4.1.1 on 2022-12-25 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0005_alter_productos_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='ID_producto'),
        ),
    ]
