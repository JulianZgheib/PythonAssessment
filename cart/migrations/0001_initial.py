# Generated by Django 4.1.1 on 2022-09-15 11:33

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groceries', '0008_remove_cart_items_cart_remove_cart_items_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField(default=0.0, validators=[django.core.validators.MinValueValidator(0, "total can't be smaller than zero")])),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceries.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Cart_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceries.products')),
            ],
        ),
    ]