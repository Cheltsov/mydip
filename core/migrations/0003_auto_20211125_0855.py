# Generated by Django 3.2.9 on 2021-11-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_user_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userextsettings',
            name='body_mass_index',
            field=models.FloatField(max_length=100, verbose_name='Индекс массы тела'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='chest_relax',
            field=models.FloatField(max_length=200, verbose_name='Грудь расслабленная'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='chest_tense',
            field=models.FloatField(max_length=200, verbose_name='Грудь напряженная'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='left_biceps_relax',
            field=models.FloatField(max_length=100, verbose_name='Левый бицепс расслабленный'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='left_biceps_tense',
            field=models.FloatField(max_length=100, verbose_name='Левый бицепс напряженный'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='left_forearm',
            field=models.FloatField(max_length=100, verbose_name='Левое предплечье'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='left_shin',
            field=models.FloatField(max_length=100, verbose_name='Голень левая'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='left_thigh',
            field=models.FloatField(max_length=100, verbose_name='Бедро левое'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='neck',
            field=models.FloatField(max_length=100, verbose_name='Шея'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='pelvis',
            field=models.FloatField(max_length=200, verbose_name='Таз'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='right_biceps_relax',
            field=models.FloatField(max_length=100, verbose_name='Правый бицепс расслабленный'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='right_biceps_tense',
            field=models.FloatField(max_length=100, verbose_name='Правый бицепс напряженный'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='right_forearm',
            field=models.FloatField(max_length=100, verbose_name='Правое предплечье'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='right_shin',
            field=models.FloatField(max_length=100, verbose_name='Голень правая'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='right_thigh',
            field=models.FloatField(max_length=100, verbose_name='Бедро правое'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='shoulders',
            field=models.FloatField(max_length=200, verbose_name='Плечи'),
        ),
        migrations.AlterField(
            model_name='userextsettings',
            name='waist',
            field=models.FloatField(max_length=200, verbose_name='Талия'),
        ),
    ]
