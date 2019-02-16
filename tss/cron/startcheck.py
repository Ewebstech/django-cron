from django.core.management.base import BaseCommand, CommandError
from tss.views.my_logger import get_logger
from django.utils import timezone

logger = get_logger()
class Command(BaseCommand):
    help = ''

    def handle(self, *args, **options):
        try:
            logger.info('Logged Command Result')
            time = timezone.now().strftime('%X')
            self.stdout.write("It's now %s" % time)
        except (Exception, CommandError):
            raise CommandError('Error Running Command') 

    