import asyncio
import requests
import tornado.web
import json

class Execute(tornado.web.RequestHandler):
    def post(self):
        byte_input = self.request.body_arguments["input"][0]
        input = byte_input.decode("utf-8")
        print("asdf")
        # GET https://newsapi.org/v2/everything?q=Apple&from=2023-02-26&sortBy=popularity&apiKey=API_KEY
        API_KEY = "183daca270264bad86fc5b72972fb82a"
        result = requests.get(
            "https://newsapi.org/v2/everything?q=" + input + "&from=2023-01-26&sortBy=popularity&apiKey=" + API_KEY)
        data = result.content.decode("utf-8")
        j = json.loads(data)
        for article in j["articles"]:
            if article["title"] is not None:
                self.write(article["title"] + "<br/>")

def make_app():
    return tornado.web.Application([
        (r"/view(.*)", tornado.web.StaticFileHandler, {'path': "static/index.html"}),
        (r"/execute", Execute)
    ])

async def main():
    app = make_app()
    app.listen(8888)
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
