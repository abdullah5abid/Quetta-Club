# Generated by Django 4.0.3 on 2022-10-04 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0018_alter_sales_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales',
            name='created_date',
            field=models.DateField(),
        ),
    ]
