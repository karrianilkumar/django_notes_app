# Generated by Django 4.2.11 on 2025-03-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
