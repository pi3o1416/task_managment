# Generated by Django 4.0.5 on 2022-06-10 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_remove_taskassignment_assighed_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksubmission',
            name='attached_file',
            field=models.FileField(upload_to='submissions/', verbose_name='Attached files'),
        ),
    ]