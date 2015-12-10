#!/usr/bin/env python
#
# Chippy Ruxpin by Next Thing Co 2015
# Powered by C.H.I.P., the world's first $9 computer!

from bottle import run, get, post, request, route, redirect
import socket

class WebFramework:
    def __init__(self,func):
        self.ip = [(s.connect(('8.8.8.8', 80)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
        print( "---------")
        print( "CHIPPY RUXPIN IS ONLINE!")
        print( "In your browser, go to " + str(self.ip) + ":8080")
        print( "---------")
        self.talkFunc = func
        
        @route('/')
        def index():
            return '''
                <form action="/" method="post">
                    What do you want Chippy Ruxpin to say? (Or type \"twitter\" followed by some search terms):<p><input name="speech" type="text" />
                    <input value="Go!" type="submit" />
                </form>
            '''
        @post('/')
        def speak():
            speech = request.forms.get('speech')            
            self.talkFunc( speech )
            redirect('/')

        run(host=self.ip, port=8080, debug=True)
