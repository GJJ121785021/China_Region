# Generated by Django 2.2.7 on 2020-03-25 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0003_auto_20200325_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chinaregions',
            name='belong_to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='under_region', to='exercise.ChinaRegions', verbose_name='上级地区(反向关联为下级)'),
        ),
    ]
