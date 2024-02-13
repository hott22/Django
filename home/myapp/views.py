from django.shortcuts import render
from django.http import HttpResponse
from random import choice, randint
from django.utils.lorem_ipsum import paragraphs,words
import logging

LOGGER = logging.getLogger(__name__)


def index(request):
    LOGGER.info('Index page!')
    return HttpResponse(f'<h1>{words(6)}</h1><br>{paragraphs(6)}')


def about(request):
    LOGGER.info('About page!')
    return HttpResponse(f'<h1>About me!</h1><br>{paragraphs(9)}')

