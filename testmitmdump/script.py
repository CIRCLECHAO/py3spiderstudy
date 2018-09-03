from mitmproxy import ctx


def request(flow):
    request = flow.request
    info = ctx.log.info
    # request.headers['User-Agent'] = 'MitmProxy'
    # # 白色log输出
    # info(str(request.headers['User-Agent']))
    # # 黄色log输出
    # ctx.log.warn(str(request.headers['User-Agent']))
    # # 红色log输出
    # ctx.log.error(str(request.headers['User-Agent']))
    url = "http://httpbin/get"
    request.url = url
    # 打印信息
    info(request.url)
    info(request.cookies)
    info(request.host)
    info(request.method)
    info(request.port)
    info(request.scheme)
