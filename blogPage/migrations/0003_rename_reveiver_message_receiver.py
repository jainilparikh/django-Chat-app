# Generated by Django 3.2 on 2021-04-12 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogPage', '0002_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='reveiver',
            new_name='receiver',
        ),
    ]
