from __future__ import absolute_import

import json
import pprint

import numpy as np
from django.http import HttpResponse
from var_dump import var_dump

import tss.views.rulesValidator
from tss.views.DjangoClient import DjangoClient
from tss.views.my_logger import get_logger

logger = get_logger()
def getVasTransactions(self):
    # Perform get request
    url = "/vas/get-vas-transactions"
    result = DjangoClient.get(self, url)
    return json.loads(result)

def validateVasTransactions(self):
    # Convert json to python array
    vasTranDict = getVasTransactions(self)
    logger.info('Logged Validate Transaction Command')
    for vasData in vasTranDict:
        var_dump(vasData)
        return HttpResponse(vasTranDict)