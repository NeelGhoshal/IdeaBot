# Generated by Django 3.1.1 on 2021-04-11 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='mob',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
