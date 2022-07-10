# Generated by Django 4.0.3 on 2022-03-24 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0010_alter_emailrecord_semester'),
        ('account', '0005_faculty_department_faculty_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personal.department'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(choices=[('Teaching Assistant', 'TA'), ('Instructor', 'Instructor'), ('Assistant Professor', 'Asst Prof'), ('Associate Professor', 'Assoc Prof'), ('Professor', 'Prof'), ('Head of Department', 'HOD')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('One', '1'), ('Two', '2'), ('Three', '3'), ('Four', '4'), ('Five', '5'), ('Six', '6'), ('Seven', '7'), ('Eight', '8')], max_length=50, null=True),
        ),
    ]