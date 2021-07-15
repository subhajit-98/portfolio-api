# Generated by Django 3.2.5 on 2021-07-15 15:25

from django.db import migrations, models
import projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, null=True, unique=True, upload_to=projects.models.modify_upload_file_name),
        ),
    ]
