import logging.handlers
import setting

LOG_FORMAT = "[%(levelname)s %(asctime)s  %(process)d %(filename)s:%(funcName)s:%(lineno)s] %(message)s"
#LOG_FORMAT = "%(asctime)s %(pathname)s %(filename)s %(funcName)s %(lineno)s %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
# logging.basicConfig(filename=setting.FlaskSettings.LOG_PATH, format=LOG_FORMAT, level=logging.INFO)
# filehandler = logging.handlers.TimedRotatingFileHandler(
#     setting.LOG_PATH, 'M', 1, 0)
# update by day at midnight
# filehandler = logging.handlers.TimedRotatingFileHandler(
#     setting.FlaskSettings.LOG_PATH, 'midnight', 1, 0)
info_logger=logging.getLogger("__info__")
we_logger=logging.getLogger("__we__")
index_logger=logging.getLogger("__index__")

info_filehandler = logging.handlers.TimedRotatingFileHandler(
    setting.FlaskSettings.INFO_LOG_PATH, 'midnight', 1, 0)
we_filehandler = logging.handlers.TimedRotatingFileHandler(
    setting.FlaskSettings.WE_LOG_PATH, 'midnight', 1, 0)

index_filehandler = logging.handlers.TimedRotatingFileHandler(
    setting.FlaskSettings.INDEX_LOG_PATH, 'midnight', 1, 0)

info_filehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
we_filehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"
index_filehandler.suffix = "%Y-%m-%d_%H-%M-%S.log"

# 打印到屏幕设置
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# 打印到文件设置
# pic_diff_logger = logging.getLogger()
info_logger.setLevel(logging.INFO)
we_logger.setLevel(logging.WARNING)
index_logger.setLevel(logging.INFO)


we_filehandler.setFormatter(logging.Formatter(LOG_FORMAT))
info_filehandler.setFormatter(logging.Formatter(LOG_FORMAT))
index_filehandler.setFormatter(logging.Formatter(LOG_FORMAT))

# pic_diff_logger.addHandler(filehandler)
# app.logger.addHandler(filehandler)
info_logger.addHandler(ch)
info_logger.addHandler(info_filehandler)
we_logger.addHandler(we_filehandler)
index_logger.addHandler(index_filehandler)