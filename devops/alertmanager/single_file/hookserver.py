import tornado.ioloop
import tornado.web
import tornado.options


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        print("hello: get")

    def post(self):
        print(f"self.request.body: {self.request.body}")
        print(f"self.request.arguments: {self.request.arguments}")
        print("hello, world!")
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(5001)
    tornado.ioloop.IOLoop.current().start()
