import azure.functions as func
from cicd.function_app import http_hello

def test_http_hello():
    req = func.HttpRequest(
        method='GET',
        url = "/api/http_hello",
        params = {'name':"pytest"},
        body=None
    )

    resp = http_hello(req)
    assert resp.status_code == 200
    assert 'Hello, pytest' in resp.get_body().decode()
    