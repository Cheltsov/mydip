# Generated by Django 3.2.9 on 2021-11-29 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20211129_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='bodyworkout',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.user'),
        ),
    ]
