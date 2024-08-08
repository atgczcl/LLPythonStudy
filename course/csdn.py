import logging
import colorlog
import builtins
import inspect
import sys
from datetime import datetime


log_format = colorlog.ColoredFormatter(
        "[%(message_log_color)s%(asctime)s %(pathname)s:%(lineno)d%(reset)s] %(log_color)s%(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "white,bg_red",
        },
        secondary_log_colors={
            "message": {
                "DEBUG": "blue",
                "INFO": "blue",
                "WARNING": "blue",
                "ERROR": "blue",
                "CRITICAL": "blue",
            },
        },
        reset=True,  # 重置颜色
        style="%",
    )
logging.basicConfig(
            filename='output.log', 
            level=logging.DEBUG, 
            encoding='utf-8',
            format='[%(asctime)s %(pathname)s:%(lineno)d] %(message)s'
            )
log = logging.getLogger()
console_handler = logging.StreamHandler()
console_handler.setFormatter(log_format)
log.addHandler(console_handler)



#字符串颜色代码
COLOR_CODES = {
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "reset": "\033[0m",
} #字符串颜色代码

def my_print(*args, sep=' ', end='\n', file=sys.stdout, flush=False):
    # 获取调用者的栈帧信息
    stack = inspect.stack()
    # 调用者信息在栈中的位置通常是第二个元素（索引为1）
    if len(stack) > 1:
        # 获取调用者的文件名和行号
        caller_frame = stack[1]
        filename = caller_frame.filename
        lineno = caller_frame.lineno
        # 为了简洁，我们只显示文件名和行号的一部分
        filename = filename.split('/')[-1]  # 假设路径是以'/'分隔的
        # 获取当前时间
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 将文件路径和行号添加到输出中
        head = (f"[{current_time} {filename}:{lineno}] ",)
        color_head = (f"{COLOR_CODES['blue']}[{current_time} {filename}:{lineno}] {COLOR_CODES['green']}",)
        color_args = color_head + args
        args = head + args

    # 将输出内容转换为字符串
    output = sep.join(map(str, args)) + end
    color_output = sep.join(map(str, color_args)) + end + COLOR_CODES["reset"]

    # 写入到标准输出
    file.write(color_output)
    if flush:
        file.flush()
    # 同时将内容写入到日志文件
    with open("output.log", 'a', encoding='utf-8') as logfile:
        logfile.write(output)

# 保存原始的 print 函数
original_print = builtins.print
# 重写 print 函数
builtins.print = my_print

log.info("This is a test.")
log.warning("This is a warning.")
log.error("This is an error.")
log.critical("This is a critical error.")
log.debug("This is a debug message.")
print("This is a normal message.")