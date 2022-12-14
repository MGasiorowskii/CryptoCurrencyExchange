# Generated by Django 4.0.7 on 2022-09-23 21:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0005_alter_wallet_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='token',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.token'),
        ),
    ]
