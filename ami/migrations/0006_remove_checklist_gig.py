# Generated by Django 2.1.7 on 2019-03-25 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ami', '0005_auto_20190325_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='gig',
        ),
    ]