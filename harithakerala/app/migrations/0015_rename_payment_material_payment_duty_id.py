# Generated by Django 4.1.3 on 2023-05-05 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_idgen_payment_id_payment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_material',
            new_name='duty_id',
        ),
    ]