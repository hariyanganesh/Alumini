# Generated by Django 2.2 on 2019-04-09 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_studinfo1_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studinfo1',
            name='id',
        ),
        migrations.AlterField(
            model_name='studinfo1',
            name='idnumber',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studinfo1',
            name='mobile',
            field=models.SmallIntegerField(null=True),
        ),
    ]