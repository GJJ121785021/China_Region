# Generated by Django 2.2.7 on 2020-03-25 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0005_auto_20200325_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chinaregions',
            name='old_name',
            field=models.CharField(default=None, max_length=30, null=True, verbose_name='曾使用过的旧名称'),
        ),
    ]
