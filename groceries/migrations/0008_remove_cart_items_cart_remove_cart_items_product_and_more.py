# Generated by Django 4.1.1 on 2022-09-15 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0007_cart_cart_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart_items',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cart_items',
            name='product',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Cart_items',
        ),
    ]
