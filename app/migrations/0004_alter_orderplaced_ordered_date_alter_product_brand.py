# Generated by Django 4.1.6 on 2023-03-15 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_cart_quantity_alter_customer_state_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='ordered_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=200),
        ),
    ]
