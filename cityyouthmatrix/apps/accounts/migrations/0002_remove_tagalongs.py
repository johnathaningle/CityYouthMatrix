# Generated by Django 3.0.7 on 2020-06-24 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='member_type',
            field=models.CharField(choices=[('C', 'Child'), ('A', 'Adult')], max_length=1),
        ),
    ]
