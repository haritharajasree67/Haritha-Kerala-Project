# Generated by Django 4.1.3 on 2023-04-17 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_wardallot'),
    ]

    operations = [
        migrations.AddField(
            model_name='idgen',
            name='cmphks_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='complainthks',
            fields=[
                ('complainthks_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('complainthks_complaint', models.CharField(max_length=50, null=True)),
                ('hks_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.harithakaramasena')),
            ],
            options={
                'db_table': 'complainthks',
            },
        ),
    ]
