# Generated by Django 4.1.6 on 2023-03-27 09:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("djstripe", "0022_sourcetransaction"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="idempotencykey",
            unique_together=set(),
        ),
    ]