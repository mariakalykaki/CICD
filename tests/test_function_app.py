import azure.functions as func
from cicd.function_app import http_trigger

def test_http_trigger():
    req = func.HttpRequest(
        method='GET',
        url = "/api/http_trigger",
        params = {'name':"pytest"},
        body=None
    )

    resp = http_trigger(req)
    assert resp.status_code == 200
    assert 'Hello, pytest' in resp.get_body().decode
    