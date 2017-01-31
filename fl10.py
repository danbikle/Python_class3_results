# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 17:23:33 2017

@author: Steve Siegel
"""

# fl10.py
# Demo:
# python fl10.py
import os
from   flask import Flask
application = Flask(__name__)
                               
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    application.run(host='0.0.0.0', port=port)
'bye'
