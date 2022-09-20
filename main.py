#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports the Google Cloud client library
from google.cloud import translate
import pyperclip
import os as o


# Instantiates a client
translate_client = translate.Client()

# Variavel de controle
controle = ''
# The target language
target = 'pt'

# Translates some text
while True:
    text = pyperclip.paste()
    tamanho = str.__len__(str(text))

    if text[tamanho - 1] == " ":
        aux = str(text)
        aux[-1].replace(" ", "")
        text = unicode(aux)

    if text != "" and text != controle:
        o.system('cls')
        translation = translate_client.translate(
            text,
            target_language=target)

        #print(u'Text: {}'.format(text))
        print(u'Translation: {}'.format(translation['translatedText']))
        controle = text