from django.urls import path
from django.conf.urls import url
from tss.views import requestHandler

urlpatterns = [
    #url(r'^vas-trans/$', rulesValidator.rulesValidator.serializeVasTransData, name='vas-trans'),
    url(r'^vas-trans/$', requestHandler.validateVasTransactions, name='vas-trans')
]