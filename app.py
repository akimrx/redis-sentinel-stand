#!/usr/bin/env python3

import time
import logging

from redis import Sentinel

logging.basicConfig(
    level="INFO",
    datefmt="%H:%M:%S",
    format="%(asctime)s %(message)s"
)
logger = logging.getLogger(__name__)
sentinels = Sentinel([
    ("redis-sentinel-stand_sentinel_1", 26379),
    ("redis-sentinel-stand_sentinel_2", 26380),
    ("redis-sentinel-stand_sentinel_3", 26381)
])


def redis_write():
    try:
        master = sentinels.master_for('test', socket_timeout=0.1)
        response = master.incr('foo')
        logger.info(f"Write: {response}, master: {sentinels.discover_master('test')}")
    except Exception as exc:
        logger.error(f"Can't write to master: {exc}")


def redis_read():
    try:
        slave = sentinels.slave_for('test', socket_timeout=0.1)
        response = slave.get('foo')
        logger.info(f"Read: {response}")
    except Exception as exc:
        logger.error(f"Can't read from slave: {exc}")


if __name__ == "__main__":
    while True:
        redis_write()
        redis_read()
        time.sleep(1)
