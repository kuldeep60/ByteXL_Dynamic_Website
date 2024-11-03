# Generated by Django 4.1.6 on 2023-03-15 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_cart_state_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhara Pardesh', 'Andhara Pardesh'), ('Arunachal Pardesh', 'Arunachal Pardesh'), ('Asam', 'Asam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Punjab', 'Punjab'), ('Rajsthan', 'Rajsthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], max_length=50),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'), ('Andhara Pardesh', 'Andhara Pardesh'), ('Arunachal Pardesh', 'Arunachal Pardesh'), ('Asam', 'Asam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Punjab', 'Punjab'), ('Rajsthan', 'Rajsthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal')], default='Pending', max_length=50),
        ),
    ]
