# Generated by Django 2.1.2 on 2018-10-07 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracking', '0002_auto_20181002_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overtime_Adjustment_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adjustment_date', models.DateField(verbose_name='adjustment_date')),
                ('adjustment', models.DecimalField(decimal_places=10, max_digits=10)),
            ],
        ),
    ]