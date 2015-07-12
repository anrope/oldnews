import tornado.ioloop
import tornado.web
import requests
import json
#from firebase import firebase

import settings

test_data = [
    {
        "url": "http://www.theguardian.com/football/2014/jul/08/germany-brazil-world-cup-semi-final-match-report",
        #"timestamp": "2014-07-08"
        "timestamp": 10
    },
    {
        "url": "http://www.cnn.com/2009/HEALTH/11/12/h1n1.flu.deaths/",
        #"timestamp": "2009-11-12"
        "timestamp": 20
    },
    {
        "url": "http://www.nbcnewyork.com/news/local/New-York-City-Celebrates-Womens-World-Cup-Winners-Parade-of-Champions-313146921.html",
        #"timestamp": "2015-07-10",
        "timestamp": 5
    }
]

class EnrichHandler(tornado.web.RequestHandler):
    embedly_call = 'http://api.embed.ly/1/extract?key={}&url={}'
    firebase_host = 'https://blazing-torch-4098.firebaseIO.com'
    def get(self):
        responses = []
        print '+++ handling request'
        for article in test_data:
            r = requests.get(self.embedly_call.format(
                settings.EMBEDLY_API_KEY, article["url"]))

            print '+++ embedly', article["url"]

            extract = r.json()

            enriched = {
                "url": article["url"],
                "timestamp": article["timestamp"],
                #"title": extract["title"],
                #"image": extract["images"][0]["url"],
                #"keywords": [k["name"] for k in extract["keywords"]],
                #"entities": [e["name"] for e in extract["entities"]],
                #"recommended": []
            }
            """
            for rel in extract["related"]:
                print '+++ related', rel["title"]
                enriched["recommended"].append({
                    "url": rel["url"],
                    "title": rel["title"],
                    "image": rel["thumbnail_url"],
                })
            """
            responses.append(enriched)

        print '+++ pushing to firebase'
        #firebase.post('/users', 'anrope-test', {'print': 'pretty'}, 'hilol')
        r = requests.post('{}/users/anrope-test.json'.format(self.firebase_host),
            data=json.dumps(responses))
        self.write(json.dumps(responses))
        self.finish()

application = tornado.web.Application([
    (r"/", EnrichHandler),
])

if __name__ == "__main__":
    #firebase = firebase.FirebaseApplication("https://blazing-torch-4098.firebaseIO.com", None)
    application.listen(8313)
    print '+++ enrichapp listening for connections'
    tornado.ioloop.IOLoop.current().start()
