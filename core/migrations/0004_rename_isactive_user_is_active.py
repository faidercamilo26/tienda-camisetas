# Generated by Django 4.2.6 on 2023-11-02 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_user_tipo_persona'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='isActive',
            new_name='is_active',
        ),
    ]