# Generated by Django 3.0.7 on 2020-06-22 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0002_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='Musician',
            new_name='musician',
        ),
    ]