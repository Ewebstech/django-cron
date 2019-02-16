import json

import numpy as np
from django.core.management.base import BaseCommand, CommandError
from django.http import HttpResponse
from django.utils import timezone
from var_dump import var_dump

from tss.views.DjangoClient import DjangoClient
from tss.views.my_logger import get_logger

logger = get_logger()
def validate_vas(self):
    logger.info('Log:: Making request to VAS server .. pulling transaction records...')
    var_dump("Log:: Making request to VAS server .. pulling transaction records...")
    url = "/vas/get-vas-transactions"
    response = DjangoClient.get(self, url)
    vasTranDict = json.loads(response)
    i = 0
    for vasData in vasTranDict:
        # do validations for multiple failed transactions
        tranStore = {}
        if vasData['status'] == 'failed' or vasData['status'] == "declined":
           # Set Validation Rules
           var_dump("Log:: Found a failed transaction")
           tranStore.update( {'' : 23} )
           var_dump(vasData) 
        else:
            wallet = vasData['wallet']
            var_dump(vasData, wallet)
            amount = vasData['numericalAmount']
            terminal = vasData['terminal']
            channel = vasData['channel']
            product = vasData['product']
            category = vasData['category']
            currencyCountry = vasData['currencyCountry']
            status = vasData['status']
            transactionRRN = vasData['status'] # is this unique for every request?
            cardPAN = vasData['status']
            transactionSTAN = vasData['transactionSTAN']
            vasCustomerAccount = vasData['vasCustomerAccount']
            paymentMethod = vasData['paymentMethod']
            vasCustomerName = vasData['vasCustomerName']
            vasCustomerAccount = vasData['vasCustomerAccount']
            vasProviderName = vasData['vasProviderName']
            vasProviderTransactionreference = vasData['vasProviderTransactionreference']
            extraJsonResponse = vasData['response']        

        i += 1
        break
    

class Command(BaseCommand):
    help = 'Validate Vas Transactions'

    def handle(self, *args, **options):
        validate_vas(self)
        try:
            
            time = timezone.now().strftime('%X')
            self.stdout.write("validate_vas--- command stopped at exactly %s" % time)
        except (Exception, CommandError):
            logger.info('Log:: Error Running Vas Command')
            raise CommandError('Error Running Command') 
