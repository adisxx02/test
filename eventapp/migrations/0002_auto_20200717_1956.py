# Generated by Django 2.1.5 on 2020-07-17 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bagian',
            old_name='judul',
            new_name='Divisi',
        ),
    ]
