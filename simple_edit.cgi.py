# -*- coding: utf-8 -*-
"""
Created on Sun Aug 11 15:02:56 2019

@author: libozhang
"""

#!/usr/bin/env python

import cgi
form=cgi.FieldStorage()

text=form.getvalue('text',open('simple_edit.dat').read())
f=open('simple_edit.dat','w')
f.write(text)
f.close()
print("""Content-type:text/html
      <html>
        <head>
          <title>A simple Editor</title>
        </head>
        <body>
            <form action='simple_edit.cgi'method='POST'>
            <textarea rows='10' cols='20' name='text'>{}</textarea><br/>
            <input type='submit'/>
            </form>
        </body>
      </html>
      """.format(text))