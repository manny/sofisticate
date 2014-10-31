import requests
import simplejson

CLARIFAI_APP_ID="zlDtrRghUoe_axX8r1Wri13PB5HK43NGV1yjbZtD"
CLARIFAI_APP_SECRET="3KyosjA58Mqz0DEAPL-c0qpQcp9onFbiIpVRsDvA"
ARTSY_CLIENT_ID="6dcb696f4076517e8d7a"
ARTSY_APP_SECRET="43551d1094a257165d8576401efcefe2"

def get_artsy_key():
    args = {'client_id': ARTSY_CLIENT_ID, 'client_secret':ARTSY_APP_SECRET}
    response = requests.post('https://api.artsy.net/api/tokens/xapp_token', params=args)
    json = simplejson.loads(response.text)
    return json['token']

