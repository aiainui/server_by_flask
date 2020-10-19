# 0 本地开发环境 1 测试环境 2 线上guest环境 3 线上环境
import os

SETTING_ENVS = 0

# 0 本地开发环境 1 测试环境 2 线上guest环境 3 线上环境
SETTING_ENVS=0

DEL_TMP_FILE=True

if SETTING_ENVS==0:
    ON_LINE=False
    DEBUG = True
    ABS_PATH = "./"
    HOME_LOG=ABS_PATH+"log/"


class FlaskSettings:
    PORT = 8431
    SERVICE_NUM = 6
    INFO_LOG_PATH = HOME_LOG + "/course_analysis"
    WE_LOG_PATH = HOME_LOG + "/course_analysis.we"
    INDEX_LOG_PATH = HOME_LOG + "/course_analysis.index"

