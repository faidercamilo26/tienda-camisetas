# Generated by Django 4.2.6 on 2023-11-03 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_rename_correo_user_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='numero_documento',
            new_name='id',
        ),
    ]