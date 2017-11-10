class element(object):
    """ """
    title = ""
    image_url = ""
    subtitle = ""
    buttons = []

def new_element(title, image, subtitle):
    """ Generate a new element """
    elem = element()
    elem.title = title
    elem.image_url = image
    elem.subtitle = subtitle
    return elem

class button(object):
    """ """
    btype = ""
    url = ""
    title = ""

def new_button(url, title, btype="web_url"):
    but = button()
    but.btype = btype
    but.url = url
    but.title = title
    return but
