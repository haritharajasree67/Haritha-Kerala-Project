# Generated by Django 4.1.3 on 2023-04-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_idgen_foodbalance_id_foodbalance'),
    ]

    operations = [
        migrations.AddField(
            model_name='function',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
