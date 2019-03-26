from django.core.management.base import BaseCommand
from django.utils import timezone

class Command(BaseCommand):
    help='Display current time'

    def handle(self,*args,**kwargs):
        time=timezone.now().strftime('%X') #strftime is the time representation format   %X - preferred time representation without the date
        self.stdout.write("It's now %s" % time)