# Generated by Django 5.1.6 on 2025-03-07 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('role', '0002_alter_role_table_alter_userrole_table'),
        ('user', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrole',
            name='role_id',
            field=models.ForeignKey(db_column='role_id', on_delete=django.db.models.deletion.CASCADE, to='role.role'),
        ),
        migrations.AlterField(
            model_name='userrole',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
