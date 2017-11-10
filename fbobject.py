import pyfbook
import json

def genQuickReply(title, value):
    """ Generate JSON objects from Facebook API """
    return {
        "content_type": "text",
        "title": title,
        "payload": value
    }

def gen_productcard(element):
    """ Return a JSON object """
    card = {}
    card['type'] = "template"
    card['payload'] = {}
    card['payload']['template_type'] = "generic"
    card['payload']['elements'] = []
    card['payload']['elements'].append(gen_element(element))
    return card
    
def gen_button(button):
    """ Return a JSON object of a button """
    but = {}
    but['type'] = button.btype
    but['url'] = button.url
    but['title'] = button.title
    return but

def gen_element(element):
    """ Return a JSON object of a element """
    elem = {}
    elem['title'] = element.title
    elem['image_url'] = element.image_url
    elem['subtitle'] = element.subtitle
    elem['buttons'] = []
    for buttons in element.buttons:
        elem['buttons'].append(gen_button(buttons))
    return elem