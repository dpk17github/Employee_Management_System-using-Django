# Generated by Django 4.1 on 2022-08-20 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng_app', '0007_role_sno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='role',
            name='id',
        ),
        migrations.AlterField(
            model_name='role',
            name='sno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
