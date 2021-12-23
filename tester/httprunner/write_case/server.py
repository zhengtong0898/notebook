import tornado.ioloop
import tornado.web
import tornado.options


class LoginHandler(tornado.web.RequestHandler):

    def post(self):
        username = self.get_argument("username")
        password = self.get_argument("password")
        if username == "zhangsan" and password == "zhangsan123":
            self.set_secure_cookie("username", username)
            self.write({"status": 200, "msg": "login success"})
        else:
            self.write({"status": 400, "msg": "login failed"})


class DashboardHandler(tornado.web.RequestHandler):

    def get(self):
        token = self.get_secure_cookie("username")
        if not token:
            self.write({"status": 400, "msg": "permission deny."})
            return

        self.write({"status": 200, "msg": "welcome to dashboard page."})


class LogoutHandler(tornado.web.RequestHandler):

    def post(self):
        token = self.get_secure_cookie("username")
        if not token:
            self.write({"status": 400, "msg": "permission deny."})
            return

        self.clear_all_cookies()
        self.write({"status": 200, "msg": "logout success"})


class UserHandler(tornado.web.RequestHandler):

    users = ["zhangsan", ]

    def get(self):
        token = self.get_secure_cookie("username")
        if not token:
            self.write({"status": 400, "msg": "permission deny."})
            return

        print(f"users: {self.users}")
        self.write({"status": 200, "msg": list(self.users)})

    def post(self):
        token = self.get_secure_cookie("username")
        if not token:
            self.write({"status": 400, "msg": "permission deny."})
            return

        username = self.get_argument("username")
        if username not in self.users:
            self.users.append(username)
        self.write({"status": 200, "msg": f"user {username} create success."})

    def delete(self):
        token = self.get_secure_cookie("username")
        if not token:
            self.write({"status": 400, "msg": "permission deny."})
            return

        username = self.get_argument("username")
        self.users.remove(username)
        self.write({"status": 200, "msg": f"user {username} delete success."})


def application():
    routers = [
        (r"/login", LoginHandler),
        (r"/dashboard", DashboardHandler),
        (r"/logout", LogoutHandler),
        (r"/user", UserHandler),
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
