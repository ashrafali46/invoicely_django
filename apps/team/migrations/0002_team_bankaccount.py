# Generated by Django 3.1.6 on 2021-03-03 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='bankaccount',
            field=models.CharField(blank=True, max_length=266, null=True),
        ),
    ]
