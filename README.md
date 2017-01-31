# Python_class3_results
Instructions: 
1.Create a folder named "fl10" to hold a new Flask app
2.In fl10, create a folder named: "static"
3.In static, create a file named: "blog.html"
4.In fl10, create a python script named: "fl10.py"
5.Put this syntax in it:

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
Run the file:
python fl10.py
________________________________________________
1. Press CTRL + ESC when instructed to do so.
2.Use a browser to study blog.html at the URL listed below:
http://localhost:5000/static/blog.html
2. Solve problem about why http://localhost:5000/static/blog.html shows "This site cannot be reached"
