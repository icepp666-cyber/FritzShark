#!/usr/bin/env python

# Simple python2/3 routine to get a SID from a FRITZ!Box thanks Turgizda for the original combi version.
# https://gist.github.com/Tugzrida/83f9118b13d6b49769eb89f18eeaf48e 
# The corresponding version for http/https automaic installed.

import os
from requests import get
from xml.etree import ElementTree
from hashlib import md5

cert = os.environ.get("CERT_PATH") or None
username = os.environ["FRITZBOX_USER"]
password = os.environ["FRITZBOX_PASS"]

challenge = ElementTree.fromstring(get("https://fritz.box/login_sid.lua", verify=cert).text)[1].text

hash = md5("{}-{}".format(challenge, password).encode("UTF-16LE")).hexdigest()

response = "{}-{}".format(challenge, hash)

print(ElementTree.fromstring(get("https://fritz.box/login_sid.lua?username={}&response={}".format(username, response), verify=cert).text)[0].text)
