# Generated by Django 4.1.3 on 2023-04-11 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='district',
            fields=[
                ('district_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('district_name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'district',
            },
        ),
        migrations.CreateModel(
            name='duty',
            fields=[
                ('duty_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('duty_name', models.CharField(max_length=50, null=True)),
                ('duty_description', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'duty',
            },
        ),
        migrations.CreateModel(
            name='fee',
            fields=[
                ('fee_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fee_name', models.CharField(max_length=50, null=True)),
                ('fee_description', models.CharField(max_length=50, null=True)),
                ('fee_amount', models.IntegerField(max_length=50, null=True)),
                ('fee_date', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'fee',
            },
        ),
        migrations.CreateModel(
            name='harithakaramasena',
            fields=[
                ('hks_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('hks_name', models.CharField(max_length=50, null=True)),
                ('hks_address', models.CharField(max_length=50, null=True)),
                ('hks_gender', models.CharField(max_length=50, null=True)),
                ('hks_age', models.CharField(max_length=50, null=True)),
                ('hks_phonenumber', models.CharField(max_length=50, null=True)),
                ('hks_email', models.CharField(max_length=50, null=True)),
                ('hks_date', models.CharField(max_length=50, null=True)),
                ('hks_photo', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'harithakaramasena',
            },
        ),
        migrations.CreateModel(
            name='house3',
            fields=[
                ('house_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('house_name', models.CharField(max_length=50, null=True)),
                ('house_ownername', models.CharField(max_length=50, null=True)),
                ('house_location', models.CharField(max_length=50, null=True)),
                ('house_address', models.CharField(max_length=50, null=True)),
                ('house_aadhar', models.CharField(max_length=50, null=True)),
                ('house_contact', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'house3',
            },
        ),
        migrations.CreateModel(
            name='idgen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('did', models.IntegerField()),
                ('fee_id', models.IntegerField()),
                ('local_id', models.IntegerField()),
                ('ward_id', models.IntegerField()),
                ('duty_id', models.IntegerField()),
                ('hks_id', models.IntegerField()),
                ('cmp_id', models.IntegerField()),
                ('request_id', models.IntegerField()),
                ('allot_id', models.IntegerField()),
                ('allothouse_id', models.IntegerField()),
            ],
            options={
                'db_table': 'idgen',
            },
        ),
        migrations.CreateModel(
            name='localbody',
            fields=[
                ('local_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('local_name', models.CharField(max_length=50, null=True)),
                ('local_category', models.CharField(max_length=50, null=True)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
            ],
            options={
                'db_table': 'localbody',
            },
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(max_length=50, null=True)),
            ],
            options={
                'db_table': 'login',
            },
        ),
        migrations.CreateModel(
            name='ward',
            fields=[
                ('ward_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('ward_number', models.CharField(max_length=50, null=True)),
                ('ward_membername', models.CharField(max_length=50, null=True)),
                ('ward_contact', models.IntegerField(max_length=50, null=True)),
                ('ward_email', models.CharField(max_length=50, null=True)),
                ('local_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.localbody')),
            ],
            options={
                'db_table': 'ward',
            },
        ),
        migrations.CreateModel(
            name='wardallot',
            fields=[
                ('allot_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('starting_date', models.CharField(max_length=50, null=True)),
                ('ending_date', models.CharField(max_length=50, null=True)),
                ('duty_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.duty')),
                ('hks_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.harithakaramasena')),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ward')),
            ],
            options={
                'db_table': 'wardallot',
            },
        ),
        migrations.CreateModel(
            name='houseallot',
            fields=[
                ('allothouse_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('hks_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.harithakaramasena')),
                ('house_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.house3')),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ward')),
            ],
            options={
                'db_table': 'houseallot',
            },
        ),
        migrations.AddField(
            model_name='house3',
            name='ward_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ward'),
        ),
        migrations.CreateModel(
            name='house',
            fields=[
                ('house_number', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('house_name', models.CharField(max_length=50, null=True)),
                ('house_ownername', models.CharField(max_length=50, null=True)),
                ('house_location', models.CharField(max_length=50, null=True)),
                ('house_address', models.CharField(max_length=50, null=True)),
                ('house_aadhar', models.CharField(max_length=50, null=True)),
                ('house_contact', models.CharField(max_length=50, null=True)),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ward')),
            ],
            options={
                'db_table': 'house',
            },
        ),
        migrations.AddField(
            model_name='harithakaramasena',
            name='ward_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ward'),
        ),
        migrations.CreateModel(
            name='complaint',
            fields=[
                ('complaint_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('complaint_complaint', models.CharField(max_length=50, null=True)),
                ('house_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.house3')),
            ],
            options={
                'db_table': 'complaint',
            },
        ),
        migrations.CreateModel(
            name='applications',
            fields=[
                ('request_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('request_name', models.CharField(max_length=50, null=True)),
                ('request_address', models.CharField(max_length=50, null=True)),
                ('request_dob', models.CharField(max_length=50, null=True)),
                ('request_gender', models.CharField(max_length=50, null=True)),
                ('request_age', models.CharField(max_length=50, null=True)),
                ('request_qualification', models.CharField(max_length=50, null=True)),
                ('request_rationcardtype', models.CharField(max_length=50, null=True)),
                ('request_income', models.CharField(max_length=50, null=True)),
                ('request_phonenumber', models.CharField(max_length=50, null=True)),
                ('request_email', models.CharField(max_length=50, null=True)),
                ('request_photo', models.CharField(max_length=50, null=True)),
                ('status', models.CharField(max_length=50, null=True)),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.district')),
                ('ward_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ward')),
            ],
            options={
                'db_table': 'applications',
            },
        ),
    ]
