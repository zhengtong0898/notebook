import time
import logging


def entrypoint():
    count = 0
    while count < 10:
        logging.info(f"entrypoint: count: {count}...")
        count += 1
        time.sleep(1)
