import urlfetch
import pyfbook

def getProfile(senderid):
    """ p """
    url = 'https://graph.facebook.com/v2.6/%s?fields=first_name,last_name,profile_pic,locale,gender&access_token=%s' % (senderid, pyfbook.ACCESS_TOKEN)
    return urlfetch.request(url).json

def getIDFirstname(senderid):
    profile = getProfile(senderid)
    return profile['first_name']