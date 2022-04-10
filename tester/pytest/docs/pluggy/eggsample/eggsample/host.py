import itertools
import random
import pluggy
from eggsample import hookspecs, lib


condiments_tray = {"pickled walnuts": 13, "steak sauce": 4, "mushy peas": 2}


class EggsellentCook:
    FAVORITE_INGREDIENTS = ("egg", "egg", "egg")

    def __init__(self, hook):
        self.hook = hook
        self.ingredients = None

    def add_ingredients(self):
        results = self.hook.eggsample_add_ingredients(
            ingredients=self.FAVORITE_INGREDIENTS
        )
        my_ingredients = list(self.FAVORITE_INGREDIENTS)
        # Each hook returns a list - so we chain this list of lists
        other_ingredients = list(itertools.chain(*results))
        self.ingredients = my_ingredients + other_ingredients

    def prepare_the_food(self):
        random.shuffle(self.ingredients)

    def serve_the_food(self):
        condiment_comments = self.hook.eggsample_prep_condiments(
            condiments=condiments_tray
        )
        print(f"Your food. Enjoy some {', '.join(self.ingredients)}")
        print(f"Some condiments? We have {', '.join(condiments_tray.keys())}")
        if any(condiment_comments):
            print("\n".join(condiment_comments))


def main():
    # 创建一个"eggsample"插件管理器
    pm = pluggy.PluginManager("eggsample")
    # 添加`hook规范签名`
    pm.add_hookspecs(hookspecs)
    # 从所有已安装的包(pip list)中检索和匹配entry_point.group == "eggsample"的插件, 并将该插件的所有`hook实现函数`注册进来.
    # 重点在这里: 后续开发的以group="eggsample"的插件, 都会被自动注册进来, 然后一起执行.
    pm.load_setuptools_entrypoints(group="eggsample")
    # 从本地的 lib 程序文件中将所有的`hook实现函数`注册进来.
    pm.register(lib)

    # 主程序按照下面这个框架来运行.
    cook = EggsellentCook(pm.hook)
    # 1. 先准备所有的材料: 执行 eggsample_add_ingredients 接口(融入更多的食材).
    cook.add_ingredients()
    # 2. 开始制作食物: shuffle(融合、搅拌、翻炒)所有的材料.
    cook.prepare_the_food()
    # 3. 上菜: 执行 eggsample_prep_condiments 接口(温馨提示: 配料清单).
    cook.serve_the_food()


if __name__ == "__main__":
    main()
