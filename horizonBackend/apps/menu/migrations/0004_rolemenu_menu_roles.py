# Generated by Django 5.1.6 on 2025-03-08 07:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menu_parent'),
        ('role', '0003_alter_userrole_role_id_alter_userrole_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_now=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.menu')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='role.role')),
            ],
            options={
                'db_table': 'role_menu',
                'unique_together': {('role', 'menu')},
            },
        ),
        migrations.AddField(
            model_name='menu',
            name='roles',
            field=models.ManyToManyField(through='menu.RoleMenu', to='role.role'),
        ),
    ]
