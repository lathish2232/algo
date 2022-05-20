import logging

from django.shortcuts import render
from django.http import JsonResponse

log = logging.getLogger(__name__)

def angelOneLogin(request):
    log.info('this is info')
    data={"msg": "welcome to angel one "}
    return JsonResponse(data)