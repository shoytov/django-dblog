# Generated by Django 3.0.8 on 2020-07-06 10:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ErrorLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250, verbose_name='Url, где произошла ошибка')),
                ('exception_name', models.CharField(max_length=250, verbose_name='Exception name')),
                ('exception', models.TextField(verbose_name='Exception')),
                ('traceback', models.TextField(verbose_name='Full Traceback')),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время ошибки')),
            ],
            options={
                'verbose_name': 'Лог ошибки',
                'verbose_name_plural': 'Логи ошибок',
            },
        ),
    ]