# Generated by Django 3.2.9 on 2021-11-29 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_goals'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGoal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='core.goals')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
    ]
