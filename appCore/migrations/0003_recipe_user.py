# Generated by Django 2.2.6 on 2022-06-26 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appUsers', '0001_initial'),
        ('appCore', '0002_auto_20220624_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='appUsers.User'),
            preserve_default=False,
        ),
    ]
