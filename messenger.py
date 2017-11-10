"""s  """
import pyfbook
import urlfetch
import json
import fbobject
import elements

def sendMessage(**kwargs):
    """ Generic function that send messages on Messenger """
    data = {}
    if kwargs.get('sender_id') is not None:
        data['recipient'] = {"id": kwargs.get('sender_id')}
        data['message'] = {}
        if kwargs.get('message') is not None:
            data['message'] = {"text": kwargs.get('message')}
        if kwargs.get('quickreplies') is not None:
            data['message']['quick_replies'] = []
            for title, value in kwargs.get('quickreplies').items():
                data['message']['quick_replies'].append(fbobject.genQuickReply(title, value))
        if kwargs.get('product_card') is not None:
            elem = pyfbook.elements.new_element("weeeee", "https://cdn.discordapp.com/attachments/256779951989194753/378566894027800588/Meow.jpg", "MEOW MEOW")
            elem.buttons.append(pyfbook.elements.new_button("http://google.com", "WAI"))
            data['message']['attachment'] = pyfbook.gen_productcard(elem)
        sendData(data)

def sendData(data):
    params = {
        "access_token": pyfbook.ACCESS_TOKEN
    }

    headers = {
        "Content-Type": "application/json"
    }
    url = "https://graph.facebook.com/v2.6/me/messages"
    urlfetch.post(url=url, headers=headers, data=json.dumps(data), params=params)