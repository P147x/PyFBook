import elements
import fbobject
import urlfetch
import json

class pyfbook(object):
    def __init__(self, token):
        self._access_token = token

    @property
    def _access_token(self):
        return self._access_token

    @_access_token.setter
    def _access_token(self, token):
        _access_token = token

    def send_message(self, **kwargs):
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
                elem = elements.new_element("weeeee", "https://cdn.discordapp.com/attachments/256779951989194753/378566894027800588/Meow.jpg", "MEOW MEOW")
                elem.buttons.append(elements.new_button("http://google.com", "WAI"))
                data['message']['attachment'] = fbobject.gen_productcard(elem)
                print data
            #sendData(data)

    def sendData(data):
        params = {
            "access_token": pyfbook.pyfbook._access_token
        }
    
        headers = {
            "Content-Type": "application/json"
        }
        url = "https://graph.facebook.com/v2.6/me/messages"
        urlfetch.post(url=url, headers=headers, data=json.dumps(data), params=params)