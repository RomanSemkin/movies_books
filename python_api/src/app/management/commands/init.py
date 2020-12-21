from os import environ

from django.core.management import call_command
from django.core.management.base import BaseCommand

from app.models import APIUser


class Command(BaseCommand):
    help = "Service Initialization"

    def handle(self, *args, **options):
        call_command("migrate")
        call_command("collectstatic", verbosity=0, interactive=False)
        self.create_administrator()

    def create_administrator(self):
        if not APIUser.objects.all().exists():
            APIUser.objects.create_superuser(
                username=environ.get("API_USER_NAME", "admin"),
                email=environ.get("API_USER_EMAIL", None),
                password=environ.get("API_USER_PASSWORD", "admin"),
            )
            self.stdout.write("Api user is created!")

