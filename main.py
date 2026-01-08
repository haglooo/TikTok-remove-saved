from concurrent.futures import ThreadPoolExecutor
from requests import get, post
import SignerPy
import random

ssid = ''
aweme_id = input('VideoID: ')


def unsave(aweme_id):
    try:
        url = 'https://api32-normal-no1a.tiktokv.eu/aweme/v1/aweme/collect/'
        params = {
            "action": "0",
            "aid": "1233",
            "app_type": "dC5tZS94ZG5pa2l0YQ",
            "app_name": "musical_ly",
            "aweme_id": aweme_id,
            "channel": "googleplay",
            "device_id": random.randint(1, 6767676767),
            "device_platform": "android",
            "device_type": "ASUS_I005DA",
            "iid": random.randint(1, 6767676767),
            "os": "android",
            "os_version": "12",
            "version_code": "430104",
            "version_name": "43.1.4"
        }
        s = SignerPy.sign(params=params, version=4404)
        headers = {
            'User-Agent': 'com.zhiliaoapp.musically/2023105030 (Linux; U; Android 11; ar; RMX3269; Build/RP1A.201005.001; Cronet/TTNetVersion:2fdb62f9 2023-09-06 QuicVersion:bb24d47c 2023-07-19)',
            'cookie': f'sessionid={ssid}',
            'x-ss-req-ticket': s['x-ss-req-ticket'],
            'x-ss-stub': s['x-ss-stub'],
            'x-gorgon': s["x-gorgon"],
            'x-khronos': s["x-khronos"],
            'x-argus': s["x-argus"],
            'x-ladon': s["x-ladon"],
            'content-type': "application/x-www-form-urlencoded"
        }
        r = get(url, params=params, headers=headers).text
        print(r)
    except Exception as e:
        print(e)
        pass

def worker():
    while True:
        unsave(aweme_id)

with ThreadPoolExecutor(max_workers=20) as executor:
    for _ in range(20):
        executor.submit(worker)
