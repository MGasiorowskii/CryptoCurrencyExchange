# Generated by Django 4.0.7 on 2022-09-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_alter_history_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date_time',
            field=models.DateTimeField(),
        ),
    ]
