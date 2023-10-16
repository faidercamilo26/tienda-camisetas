# Generated by Django 4.2.6 on 2023-10-16 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authApp', '0003_alter_camisetacolor_idcamisetacolor_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='contraseña',
        ),
        migrations.AddField(
            model_name='persona',
            name='groups',
            field=models.ManyToManyField(related_name='personas', to='auth.group'),
        ),
        migrations.AddField(
            model_name='persona',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='persona',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='persona',
            name='password',
            field=models.CharField(default=' ', max_length=30, verbose_name='Password'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='user_permissions',
            field=models.ManyToManyField(related_name='personas_permissions', to='auth.permission'),
        ),
        migrations.AddField(
            model_name='persona',
            name='username',
            field=models.CharField(default='faidercamil', max_length=20, unique=True, verbose_name='Username'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='persona',
            name='correo',
            field=models.CharField(max_length=30, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dirreccion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=20, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='numeroCelular',
            field=models.IntegerField(unique=True),
        ),
    ]
