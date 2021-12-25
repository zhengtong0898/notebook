import requests


def scenario_1():
    """
    测试场景-1
    登录成功后, 可以正常访问/dashboard接口.
    """
    session = requests.session()

    # 登录
    resp = session.post("http://127.0.0.1:8888/login", data={"username": "zhangsan", "password": "zhangsan123"})
    assert resp.json()["status"] == 200

    # 访问 /dashboard 接口
    resp = session.get("http://127.0.0.1:8888/dashboard")
    assert resp.json()["status"] == 200


def scenario_2():
    """
    测试场景-2
    直接访问/dashboard接口, 没有权限.
    """
    session = requests.session()

    # 访问 /dashboard 接口
    resp = session.get("http://127.0.0.1:8888/dashboard")
    assert resp.json()["status"] == 400


def main():
    scenario_1()
    scenario_2()


if __name__ == '__main__':
    main()
