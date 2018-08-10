import requests, bs4, os
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404

os.chdir("E:\\Programas\\helloworld\\website\\templates\\website")

exampleFile = open("index.html")
exampleSoup = bs4.BeautifulSoup(exampleFile)
elements = exampleSoup.select('#edtprotocolo')

# print('Item 1', type(elements))
# print('Item 2', len(elements))
# print('Item 3', type(elements[0]))
# print('Item 4', str(elements[0]))
# print('Item 5', str(elements[0].attrs))

# spamElem = exampleSoup.select('input')[0]
# print(str(spamElem))
# print(str(spamElem.get('id')))

spamElem = exampleSoup.select('input')
# print(spamElem[0])
# print(spamElem[0].getText())
print(spamElem[0].get('id'))
print(spamElem[0].get('value'))


# print(spamElem[1])
# print(spamElem[1].getText())
print(spamElem[1].get('id'))

# print(spamElem[2])
# print(spamElem[2].getText())
print(spamElem[2].get('name'))

    
