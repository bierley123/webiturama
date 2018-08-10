from django import template
from django.template.defaultfilters import stringfilter
import requests, bs4, os
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
import ctypes

register = template.Library()


@register.filter
@stringfilter
def numero_atual(value):
    """ 		Retornar o numero     """
    try:
        path = os.path.split(os.path.abspath(__file__))[0]
        path = path + "\\atual.txt"

        print(path)
    
        with open(path) as arquivo:
            tudo = arquivo.read()    
        
        print(tudo)

        return int(tudo)
    except:
        return '0'   
     
        

