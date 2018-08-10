# -*- coding: utf-8 -*-
import requests, bs4, os
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
import ctypes

#ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

def RetornarNumero():
    try:
        path = os.path.split(os.path.abspath(__file__))[0]
        path = path + "\\atual.txt"
    
        with open(path) as arquivo:
            tudo = arquivo.read()    

        return tudo
    except:
        return '0'   
        