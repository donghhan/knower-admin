from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User

seeder = Seed.seeder(locale="ko_KR")


class Command(BaseCommand):
    help = "Creating fake user data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, help="How many users do you want to create"
        )

    def handle(self, *args, **kwargs):
        number = kwargs.get("number")
        seeder.add_entity(
            User,
            number,
            {
                "email": lambda x: seeder.faker.email(),
                "phone_number": lambda x: seeder.faker.phone_number(),
                "is_staff": False,
                "is_active": True,
            },
        )
        seeder.execute()

        self.stdout.write(self.style.SUCCES(f"{number} fake users created!"))
