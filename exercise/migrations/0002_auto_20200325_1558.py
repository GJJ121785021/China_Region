# Generated by Django 2.2.7 on 2020-03-25 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chinaregions',
            old_name='region_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='chinaregions',
            name='code',
            field=models.CharField(default=None, max_length=12, verbose_name='编号'),
        ),
    ]
