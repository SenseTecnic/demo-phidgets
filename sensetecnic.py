'''
Created on Jul 7, 2010

@author: mike
'''

import urllib
import urllib2
import base64

STS_BASE_URL='http://wotkit.sensetecnic.com/api'

def setSTSBaseUrl(url):
    STS_BASE_URL = url
    
def sendData(sensor, user, password, attributes, serverUrl=None):
    encoded_args = urllib.urlencode(attributes)
    
    # send authorization headers premptively otherwise we get redirected to a login page
    base64string = base64.encodestring('%s:%s' % (user, password))[:-1]
    
    headers = {
        'User-Agent': 'httplib',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': "Basic %s" % base64string
    }
    
    url = STS_BASE_URL+'/sensors/'+sensor+'/data'
    if(serverUrl is not None):
        url = serverUrl+'/sensors/'+sensor+'/data'

    req = urllib2.Request(url,encoded_args,headers)
    try:
        print 'Sending req: %s' % url
        urllib2.urlopen(req)
    except urllib2.URLError, e:
        print 'error - sending to url: %s' % url
        print 'error - sending event to sensor: %s' % (sensor)
        print e.reason
        return -1

    return 0


    
