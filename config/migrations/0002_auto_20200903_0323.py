# Generated by Django 2.2.6 on 2020-09-03 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-weight'], 'verbose_name': '友链', 'verbose_name_plural': '友链'},
        ),
    ]