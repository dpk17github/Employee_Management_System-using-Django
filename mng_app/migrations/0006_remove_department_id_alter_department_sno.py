# Generated by Django 4.1 on 2022-08-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng_app', '0005_department_sno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='id',
        ),
        migrations.AlterField(
            model_name='department',
            name='sno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
