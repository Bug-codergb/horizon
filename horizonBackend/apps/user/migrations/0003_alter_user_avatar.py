# Generated by Django 5.1.6 on 2025-03-05 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0002_alter_file_table'),
        ('user', '0002_alter_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ForeignKey(db_column='avatar', null=True, on_delete=django.db.models.deletion.SET_NULL, to='file.file', verbose_name='用户头像'),
        ),
    ]
