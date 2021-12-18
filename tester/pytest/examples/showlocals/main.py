import time
import logging


def entrypoint():
    count = 0
    while count < 10:
        temp_var = {"temp": "var"}
        logging.info(f"entrypoint: count: {count}...")
        count += 1
        time.sleep(1)
    aa(count)


def aa(variable_a):
    variable_b = {"hello": "world"}
    variable_c = ("godw", "pppp")
    bb(variable_b, variable_c)


def bb(vb, vc):
   cc(vc)


def cc(final):
    assert final == 1
