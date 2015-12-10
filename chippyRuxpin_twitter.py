#!/usr/bin/env python
#
# Chippy Ruxpin by Next Thing Co 2015
# Powered by C.H.I.P., the world's first $9 computer!

# See the README.md file for instructions on how to set up your twitter account.

import twitter

class ChippyTwitter:
    def __init__(self,consumerKey,consumerSecret,accessTokenKey,accessTokenSecret):
        self.api = twitter.Api()
        self.api = twitter.Api(consumer_key=consumerKey,consumer_secret=consumerSecret, access_token_key=accessTokenKey, access_token_secret=accessTokenSecret)
    
    def getTweet(self,text):
        search = self.api.GetSearch( term=text, lang='en', result_type='recent', count=1, max_id='')
        result = ""
        for t in search:
            result = " @ " + t.user.screen_name + " says: " + t.text.encode('ascii', 'ignore').decode('ascii')
        
        print( result )
            
        result = result.replace(" @", "  at ")
        result = result.replace(":)", " smiley face")
        result = result.replace(":D", " smiley face")
        result = result.replace(":(", " frowny face")
        result = result.replace("#", " hash tag ")
        result = result.replace( "&amp;", " and ")
        result = result.replace( "\n", " " ) #Remove line breaks.
        result = result.replace("nextthingco", "next-thing-co ") #Make our company name sound better.
        result = result.replace( "C.H.I.P.", "CHIP" ) #Periods drives text-to-speech a little crazy.
        result = result.replace(" RT ", " retweeting ")
	
	try:
		# Remove any URLs from this tweet.
		index = result.find( "http")
		urlString = ""
		while( index < len(result ) and result[index] != " " ):
			urlString = urlString + result[index]
			index = index + 1

		result = result.replace( urlString, "" )
	except:
		print( "URL removal failed" )

        return result
