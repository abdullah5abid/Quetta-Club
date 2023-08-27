# Generated by Django 4.1 on 2022-09-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Customers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_name", models.CharField(max_length=25)),
                ("customer_rank", models.CharField(max_length=20)),
                ("customer_id", models.CharField(max_length=10)),
                ("customer_file", models.FileField(upload_to="media/")),
            ],
        ),
    ]
