import tornado.ioloop
import tornado.web
import tornado.options


class MainHandler(tornado.web.RequestHandler):

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        if username == "zhangsan" and password == "zhangsan123":
            self.set_secure_cookie("username", username)
            self.write({"status": 200, "msg": "login success"})
        else:
            self.set_status(400)
            self.write({"status": 400, "msg": "login error"})


class Dashboard(tornado.web.RequestHandler):

    def get(self):
        token = self.get_secure_cookie("username")
        if token:
            self.write({"status": 200, "msg": "welcome to dashboard page."})
        else:
            self.write({"status": 400, "msg": "permission deny."})


def application():
    routers = [
        (r"/login", MainHandler),
        (r"/dashboard", Dashboard),
    ]
    settings = dict(
        cookie_secret="aGVsbG8gd29ybGQh",
        login_url="/login",
        debug=True,
    )
    return tornado.web.Application(handlers=routers, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = application()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
