# Generated by Django 4.1.3 on 2023-05-04 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_housecollectiondetails_collection_material'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='housecollectiondetails',
            name='collection_material',
        ),
        migrations.AddField(
            model_name='housecollectiondetails',
            name='duty_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.duty'),
            preserve_default=False,
        ),
    ]
