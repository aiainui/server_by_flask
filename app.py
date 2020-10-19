# -*- coding: utf-8 -*-
# from gevent import monkey
# monkey.patch_all()

from flask import Flask
from flask import render_template, request, jsonify, json, make_response
from flask_cors import CORS
import os
import time
import threading
import shutil
import setting

# from img_get_feature.get_pre_split import *


# debug
# import ptvsd
# ptvsd.enable_attach(address = ('0.0.0.0', 5678))
# ptvsd.wait_for_attach()
# import socket
# try:
#     address = ('127.0.0.1', 11111)
#     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#     s.bind(address)
# except socket.error:
#     ptvsd.settrace(None, ('0.0.0.0', 5678))
# ptvsd.enable_attach(address = ('0.0.0.0', 8431))
# ptvsd.wait_for_attach()

app = Flask(__name__)
CORS(app, resources=r'/*')

from datetime import timedelta
# from logger import info_logger, we_logger

print("start successfully!")
#
def create_tmp_file():
    tmp_dir = setting.ABS_PATH + "data"
    #info_logger.info("remove_tmp_file: " + str(tmp_dir))
    res = True
    try:
        # os.remove(video_file)
        #info_logger.info("init creat dir: " + str(tmp_dir))
        if os.path.exists(tmp_dir) == True:
            shutil.rmtree(tmp_dir)
        os.mkdir(tmp_dir)
    except:
        res = False
        #info_logger.info("remove_tmp_file: " + str(video_file) + " fail!!!")
        pass

# 设置静态文件缓存过期时间
app.send_file_max_age_default = timedelta(seconds=1)


@app.route("/")
def index():
    return "ok!!"


@app.route("/call_back", methods=['POST'])
def get_res():
    data = {}

    try:
        #data = json.loads(request.data.decode('utf-8'))
        data = request.json
    except:
        pass

    print('response res-----------------------', data)
    print('\n\n\n')
    if data['code'] == 20000:
        with open('./video_url_emotion.txt', 'a') as rf:
            rf.write(str(data['requestId'])+'\t'+str(data['data']['emotion']['total']['score']) + '\n')

    return cross_make_response(jsonify(data))

def cross_make_response(json_info):
    response = make_response(json_info)
    response.headers['Content-Type'] = 'text/html'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'OPTIONS,HEAD,POST,GET'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
    return response
