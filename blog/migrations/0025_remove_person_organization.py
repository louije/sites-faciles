# Generated by Django 5.0.6 on 2024-07-08 15:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0024_transfer_organizations"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="person",
            name="organization",
        ),
    ]