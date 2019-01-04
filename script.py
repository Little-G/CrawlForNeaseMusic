import subprocess
import logging

def check_configue():

    import base64
    import re
    logging.basicConfig(filename='script.log',level=logging.ERROR)

    try:
        from bs4 import BeautifulSoup
    except:
        try:
            subprocess.call('sudo pip install Beautifulsoup4', shell=True)
        except:
            logging.error(str(Exception))

    try:
        import requests
    except:
        subprocess.call('sudo pip install requests', shell=True)

    try:
        from requests_html import HTMLSession
    except:
        subprocess.call('sudo pip install requests-html', shell=True)

    try:
        from Crypto.Cipher import AES
    except:
        subprocess.call('sudo pip install pycrpto', shell=True)

    try:
        import pandas as pd
    except:
        subprocess.call('sudo pip install pandas', shell=True)

    try:
        import numpy as np
    except:
        subprocess.call('sudo pip install numpy', shell=True)


