# Generated by Django 5.0.3 on 2024-04-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0016_delete_com_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Com_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('service_id', models.CharField(max_length=100)),
                ('service_name', models.CharField(max_length=100)),
                ('phno', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('add1', models.CharField(max_length=255)),
                ('add2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('pincode', models.CharField(max_length=20)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('completed_on', models.DateTimeField(auto_now_add=True)),
                ('placed_on', models.DateTimeField()),
            ],
        ),
    ]
