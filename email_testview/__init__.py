from django.utils.module_loading import autodiscover_modules
from .registry import registry

# -*- coding: utf-8 -*-
__version__ = '0.1.0'



def autodiscover_emails():
    autodiscover_modules('emails', register_to=registry)
