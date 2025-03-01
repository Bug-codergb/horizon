# Generated by Django 5.1.6 on 2025-02-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0004_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='用户名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('description', models.TextField(verbose_name='描述')),
                ('create_time', models.DateField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
    ]
