# Generated by Django 4.1 on 2022-08-20 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mng_app', '0003_remove_employee_id_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
    ]
