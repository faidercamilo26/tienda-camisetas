# Generated by Django 4.2.6 on 2023-11-02 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_user_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='correo',
            field=models.EmailField(max_length=30, unique=True, verbose_name='Email'),
        ),
    ]