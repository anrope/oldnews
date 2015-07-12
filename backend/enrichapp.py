import tornado.ioloop
import tornado.web
import requests
import json

import settings

test_data = [
    {
        "url": "http://www.theguardian.com/football/2014/jul/08/germany-brazil-world-cup-semi-final-match-report",
        "timestamp": "2014-07-08"
    },
    {
        "url": "http://www.cnn.com/2009/HEALTH/11/12/h1n1.flu.deaths/",
        "timestamp": "2009-11-12"
    },
    {
        "url": "http://www.nbcnewyork.com/news/local/New-York-City-Celebrates-Womens-World-Cup-Winners-Parade-of-Champions-313146921.html",
        "timestamp": "2015-07-10",
    },
    {
        "url": "http://www.nytimes.com/2012/07/13/arts/design/b-out.html",
        "timestamp": "2012-07-12"
    },
    {
        "url": "https://www.washingtonpost.com/blogs/worldviews/wp/2013/07/12/a-trip-to-the-roof-of-the-world/",
        "timestamp": "2013-07-12"
    },
    {
        "url": "http://www.washingtonpost.com/blogs/federal-eye/wp/2013/07/15/dhs-warns-employees-not-to-read-leaked-nsa-information/",
        "timestamp": "2013-07-12"
    },
    {
        "url": "http://www.wsj.com/articles/russia-writes-off-cuba-debt-1405083869",
        "timestamp": "2014-07-12"
    },
    {
        "url": "http://www.wsj.com/articles/north-korea-launches-two-short-range-missiles-1405222190",
        "timestamp": "2014-07-12"
    },
    {
        "url": "http://www.boston.com/news/local/massachusetts/articles/2011/07/12/prosecutors_detail_life_on_lam_with_bulger/",
        "timestamp": "2011-07-12"
    },
    {
        "url": "http://techcrunch.com/2011/07/12/confirmed-ea-buys-popcap-games-for-750-million-plus-earn-out/",
        "timestamp": "2011-07-12"
    },
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
                "title": extract["title"],
                "description": extract["description"],
                "image": extract["images"][0]["url"],
                "keywords": [k["name"] for k in extract["keywords"]],
                "entities": [e["name"] for e in extract["entities"]],
                "recommended": []
            }

            for rel in extract["related"]:
                print '+++ related', rel["title"]
                enriched["recommended"].append({
                    "url": rel["url"],
                    "title": rel["title"],
                    "image": rel["thumbnail_url"],
                })

            responses.append(enriched)

        print '+++ pushing to firebase'
        r = requests.put('{}/users/anrope-test.json'.format(self.firebase_host),
            data=json.dumps(responses))
        self.write(json.dumps(responses))
        self.finish()

application = tornado.web.Application([
    (r"/", EnrichHandler),
])

if __name__ == "__main__":
    application.listen(8313)
    print '+++ enrichapp listening for connections'
    tornado.ioloop.IOLoop.current().start()
