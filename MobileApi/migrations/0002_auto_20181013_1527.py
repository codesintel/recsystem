# Generated by Django 2.1.1 on 2018-10-13 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MobileApi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recommendeditems',
            old_name='ItemID',
            new_name='ProductId',
        ),
        migrations.RemoveField(
            model_name='recommendeditems',
            name='ItemName',
        ),
        migrations.RemoveField(
            model_name='recommendeditems',
            name='TimeStamp',
        ),
    ]
