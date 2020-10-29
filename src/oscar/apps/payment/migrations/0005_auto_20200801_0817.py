# Generated by Django 3.0.8 on 2020-08-01 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20181115_1953'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'ordering': ['pk'], 'verbose_name': 'Source', 'verbose_name_plural': 'Sources'},
        ),
        migrations.AlterModelOptions(
            name='sourcetype',
            options={'ordering': ['name'], 'verbose_name': 'Source Type', 'verbose_name_plural': 'Source Types'},
        ),
        migrations.AlterField(
            model_name='sourcetype',
            name='name',
            field=models.CharField(db_index=True, max_length=128, verbose_name='Name'),
        ),
    ]
