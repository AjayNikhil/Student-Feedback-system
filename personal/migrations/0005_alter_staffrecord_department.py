# Generated by Django 4.0.3 on 2022-03-16 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0004_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffrecord',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personal.department'),
        ),
    ]
