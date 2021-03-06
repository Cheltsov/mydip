# Generated by Django 3.2.9 on 2021-11-29 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_bodyworkout_goal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bodyexercise',
            name='description',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='bodyexercise',
            name='image',
            field=models.URLField(null=True, verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='bodyexercise',
            name='main_muscles',
            field=models.TextField(null=True, verbose_name='Основные мышцы'),
        ),
        migrations.AlterField(
            model_name='bodyexercise',
            name='minor_muscles',
            field=models.TextField(null=True, verbose_name='Второстепенные мышцы'),
        ),
        migrations.AlterField(
            model_name='bodyexercise',
            name='sport_equipment',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='bodyworkout',
            name='goal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.goals'),
        ),
    ]
