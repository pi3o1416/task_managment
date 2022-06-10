# Generated by Django 4.0.5 on 2022-06-10 04:42

from django.db import migrations, models
import task.services


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_alter_tasksubmission_attached_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasksubmission',
            name='attached_file',
            field=models.FileField(upload_to=task.services.get_file_path, verbose_name='Attached files'),
        ),
    ]