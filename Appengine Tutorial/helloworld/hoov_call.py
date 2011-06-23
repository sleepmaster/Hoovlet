import httplib2
import time, datetime, simplejson
import web
import hoover
from hoover import LogglySession

def get_data(logglyname, logglypass, logglysub):
        print logglyname
        print logglypass
        print logglysub
        hoover_4 = hoover.LogglySession(logglysub, logglyname, logglypass)
        #print hoover_4
        bool_val =  bool(hoover_4) 
        if True:
	        geekceo = hoover_4.inputs
 	else:
 		return bool_val
        #print geekceo
        #response = geekceo.facets(q='*.*', facetby = 'http', starttime='NOW-10DAYS', endtime='NOW-1MINUTE', buckets=10)

        #for k in geekceo:
        #       print "%s" % k

        return geekceo
# serve as a web app
urls = (
       '/blah/','blah'
)

app = web.application(urls, globals())

class blah:
      def POST(self):
      		params = web.input()
   		print get_data(params.logglyname, params.logglypass, params.logglysub)
   		stuff = get_data(params.logglyname, params.logglypass, params.logglysub)
               	return stuff

if __name__ == "__main__":
	app.run()







