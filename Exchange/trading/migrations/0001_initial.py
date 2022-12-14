# Generated by Django 4.0.7 on 2022-09-30 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wallet', '0006_alter_wallet_owner_alter_wallet_token'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='WithdrawalDepositHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0.0)),
                ('date_time', models.DateTimeField()),
                ('type', models.TextField()),
                ('address', models.FloatField(blank=True)),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.token')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TradingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.FloatField(default=0.0)),
                ('date_time', models.DateTimeField()),
                ('type', models.TextField()),
                ('transaction_price', models.FloatField()),
                ('token', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.token')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
