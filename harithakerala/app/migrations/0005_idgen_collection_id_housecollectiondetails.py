# Generated by Django 4.1.3 on 2023-04-17 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_idgen_cmphks_id_complainthks'),
    ]

    operations = [
        migrations.AddField(
            model_name='idgen',
            name='collection_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='housecollectiondetails',
            fields=[
                ('collection_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('collection_month', models.CharField(max_length=50, null=True)),
                ('collection_year', models.CharField(max_length=50, null=True)),
                ('collection_date', models.CharField(max_length=50, null=True)),
                ('collection_fee', models.CharField(max_length=50, null=True)),
                ('house_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.house3')),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ward')),
            ],
            options={
                'db_table': 'housecollectiondetails',
            },
        ),
    ]