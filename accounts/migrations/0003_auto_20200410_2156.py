# Generated by Django 3.0.3 on 2020-04-10 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200410_2143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Make', models.CharField(max_length=64, null=True)),
                ('Model', models.CharField(max_length=64, null=True)),
                ('Year', models.CharField(max_length=64, null=True)),
                ('VIN', models.CharField(max_length=64, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(null=True)),
                ('Order_amount', models.FloatField(max_length=64, null=True)),
                ('Order_status', models.CharField(choices=[('Completed', 'Completed'), ('In Progress', 'In Progress'), ('Cancelled', 'Cancelled')], max_length=64, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='date_of_birth',
            field=models.DateTimeField(null=True),
        ),
    ]
