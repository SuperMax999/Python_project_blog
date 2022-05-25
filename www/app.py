# 博客APP编写 day-2: APP骨架

import logging
import asyncio  # 参考第25章第一节
import os  # 参考15章
import json  # 参考第15章
import time
from datetime import datetime  # 参考第18章
from aiohttp import web  # 参考第25章
logging.basicConfig(level=logging.INFO)  # 参考第14章，定义错误级别

# 本文件放到www目录下。本节来编写一个异步网络框架


async def index(request):
    """定义服务器响应返回的函数"""
    return web.Response(body=b'<h1>Welcome</h1>', content_type='text/html')


async def init():
    app = web.Application()
    app.router.add_get('/', index)  # 添加URL处理的方法
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 9000)  # 创建TCP链接
    await site.start()
    logging.info('server started at http://127.0.0.1:9000...')
    return site


loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
# 浏览器上输入http://127.0.0.1:9000/即可看到界面
