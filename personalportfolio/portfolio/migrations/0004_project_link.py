# Generated by Django 5.0.4 on 2024-05-11 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
