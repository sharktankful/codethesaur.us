# Generated by Django 4.0.3 on 2022-03-10 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lookupdata',
            name='version1',
            field=models.CharField(default='', max_length=20),

        ),
        migrations.AddField(
            model_name='lookupdata',
            name='version2',
            field=models.CharField(default='', max_length=20),
        ),
    ]
