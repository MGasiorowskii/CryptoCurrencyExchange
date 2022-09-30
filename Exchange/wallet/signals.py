from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models.wallet import Wallet
from .models.token import Token
from bitcoin import random_key, privtoaddr
from eth_account import Account
import secrets
from typing import Type


@receiver(post_save, sender=User)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        create_bitcoin_wallet(instance, "bitcoin")
        create_ethereum_wallet(instance, "ethereum")
        create_ethereum_wallet(instance, "tether")


def create_bitcoin_wallet(instance: Type[Wallet], token: str) -> None:
    private_key = random_key()
    wallet_address = privtoaddr(private_key)
    token_object = Token.objects.get(name=token)

    Wallet.objects.create(owner=instance,
                          token=token_object,
                          address=wallet_address)


def create_ethereum_wallet(instance: Type[Wallet], token: str) -> None:
    private_key = "0x" + secrets.token_hex(32)
    account = Account.from_key(private_key)
    wallet_address = account.address
    token_object = Token.objects.get(name=token)

    Wallet.objects.create(owner=instance,
                          token=token_object,
                          address=wallet_address)
