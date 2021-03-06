# Generated by Django 2.0.3 on 2018-07-31 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20180731_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Confirmations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=40)),
                ('pizza_type', models.CharField(max_length=40, null=True)),
                ('size', models.CharField(max_length=15, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('username', models.CharField(max_length=30)),
                ('time', models.DateTimeField(auto_now=True)),
                ('order_status', models.CharField(default='Draft', max_length=10)),
                ('pizza_toppings', models.ManyToManyField(related_name='confirmations', to='orders.Toppings')),
                ('sub_additions', models.ManyToManyField(related_name='confirmations', to='orders.Additions')),
            ],
        ),
    ]
