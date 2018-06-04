from django.core.management import BaseCommand

    #The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    help = "My test command"
    def handle(self, *args, **options):
        self.stdout.write("Doing All The Things!")
