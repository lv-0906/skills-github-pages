import http.client
import json

def h5_login():
    conn = http.client.HTTPSConnection("locker-api.wegui.cn")
    payload = json.dumps({
    "anonymous_open_id": "754fd3e9-957c-4827-8942-f01b561ccf01",
    "social_id": "1762735967245774848"
    })
    headers = {
    'Xi-App-Id': '0a60f00b28c849d3ac529994f98b825f'
    }
    conn.request("POST", "/v1/auth/h5_login_anonymous/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    token = json.loads(data)['Result']['access_token']
    return token
def get_client():
    token = h5_login()
    conn = http.client.HTTPSConnection("locker-api.wegui.cn")
    payload = json.dumps({
    "is_create_order": True,
    "scene": "c98896302931"
    })
    headers = {
    'Authorization': f'Motern {token}',
    'Xi-App-Id': '0a60f00b28c849d3ac529994f98b825f'
    }
    conn.request("POST", "/v1/info/cabinet/", payload, headers)
    res = conn.getresponse()
    data = res.read()
    fetch_type = json.loads(data)['Result']['site']['fetch_types']
    return fetch_type