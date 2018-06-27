# -*- coding:utf-8 -*-

import conf
import json
import logging
import socket
from task_interact import glb_task_interact


class NetOpt(object):
    def __init__(self):
        pass

    def listen_tasks(self):
        skt = socket.socket()
        skt.bind(("", conf.listen_task_port))
        skt.listen(1)

        while 1:
            cli, addr = skt.accept()
            req_data = ""
            while True:
                data = cli.recv(1024)
                if not data:
                    break
                req_data += data
            cli.close()
            reqs_dict = self.__structuring_reqs(req_data)
            task_rst = glb_task_interact.exeTask(reqs_dict)
            print task_rst

    # 请求结构化
    # {id: (req_mod, url, header, post_data)}
    # header: {key: val}
    # post_data: {key: val}
    def __structuring_reqs(self, reqs_str):
        json_struct = None
        try:
            json_struct = json.loads(reqs_str)
        except:
            pass
        return json_struct


glb_net_opt = NetOpt()
