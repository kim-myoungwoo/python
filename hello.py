#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''<p>Hello, World!</p><br>
            <p>안녕 하세요!</p>'''


# In[ ]:


Flask.__

