# Generated by Django 4.2.1 on 2023-06-02 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommApp', '0005_remove_products_productname'),
    ]

    operations = [
        migrations.CreateModel(
            name='myOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Items_Json', models.CharField(max_length=5000)),
                ('First_Name', models.CharField(max_length=90)),
                ('second_Name', models.CharField(max_length=90)),
                ('Email', models.CharField(max_length=90)),
                ('phone', models.IntegerField(default=0)),
                ('Address1', models.CharField(max_length=200)),
                ('Address2', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=100)),
                ('State', models.CharField(max_length=100)),
                ('Pin_code', models.CharField(max_length=100)),
            ],
        ),
    ]