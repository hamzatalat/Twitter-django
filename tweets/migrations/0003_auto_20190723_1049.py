# Generated by Django 2.2.3 on 2019-07-23 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20190723_1047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='text',
            new_name='comment',
        ),
    ]
