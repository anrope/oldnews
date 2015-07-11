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
    }
]

class EnrichHandler(tornado.web.RequestHandler):
    embedly_call = 'http://api.embed.ly/1/extract?key={}&url={}'
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

        print '+++ finishing'
        self.write(json.dumps(responses))
        self.finish()

application = tornado.web.Application([
    (r"/", EnrichHandler),
])

if __name__ == "__main__":
    application.listen(8313)
    print '+++ enrichapp listening for connections'
    tornado.ioloop.IOLoop.current().start()
