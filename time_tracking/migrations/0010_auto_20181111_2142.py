# Generated by Django 2.1.1 on 2018-11-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracking', '0009_auto_20181104_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overtime_entry',
            name='overtime',
        ),
        migrations.RemoveField(
            model_name='overtime_entry',
            name='type',
        ),
        migrations.RemoveField(
            model_name='settingsmodel',
            name='work_time_tur',
        ),
        migrations.AddField(
            model_name='overtime_entry',
            name='adj_overtime',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Überstunden'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='overtime_entry',
            name='reg_overtime',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Überstunden'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settingsmodel',
            name='work_time_tue',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Arbeitszeit Dienstag'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='overtime_entry',
            name='overtime_date',
            field=models.DateField(unique=True, verbose_name='Datum'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='work_time_fri',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Arbeitszeit Freitag'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='work_time_mon',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Arbeitszeit Montag'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='work_time_sat',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Arbeitszeit Samstag'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='work_time_sun',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Arbeitszeit Sonntag'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='work_time_thu',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Arbeitszeit Donnerstag'),
        ),
        migrations.AlterField(
            model_name='settingsmodel',
            name='work_time_wed',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Arbeitszeit Mittwoch'),
        ),
    ]