# -*- coding:utf-8 -*-

import logging
logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s|%(levelname)s|%(filename)s:%(lineno)d|%(message)s',
    datefmt = '%Y%m%d_%H%M%S',
    filename = './ou.log',
    filemode = 'w'
)
from net_opt import glb_net_opt

def main():
    glb_net_opt.listen_tasks()


if __name__ == "__main__":
    main()
