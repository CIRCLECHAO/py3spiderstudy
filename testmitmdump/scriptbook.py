from mitmproxy import ctx


def response(flow):
    response = flow.response
    request = flow.request
    print(request.url)
    print(response.text)
