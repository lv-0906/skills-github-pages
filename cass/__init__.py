from available_locker import FindLocker
__all__=['FindLocker']

class LoggerWriter:
    def __init__(self, level):
        self.level = level

    def write(self, message):
        if message.strip():
            self.level(message)

    def flush(self):
        pass

def setup_log_redirect():
    """初始化日志重定向"""
    import sys
    import logging
    sys.stdout = LoggerWriter(logging.info)
    sys.stderr = LoggerWriter(logging.error)