import requests
from starbucks import base_url
from starbucks.utils import remove_keys_recursively
import os

headers = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8",
    "cookie": "fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=zDz3dkC5iUNiITh/WGqd/yT1CgLQOBBHD8160GQh36E=; optimizelyEndUserId=oeu1734262885695r0.9435912370295745; _gid=GA1.2.2090719523.1734262888; _gcl_au=1.1.1800411924.1734262888; ux_exp_id=58682600-9719-43dc-8ed2-c9b1e5c1348d; ASLBSA=00038f952e2a0e4383b269b31ee1c78eb55416d298f826927ef4ff9ef6ab361c81bb; ASLBSACORS=00038f952e2a0e4383b269b31ee1c78eb55416d298f826927ef4ff9ef6ab361c81bb; optimizelySession=0; tiWQK2tY=A06aH8qTAQAAdpROAMyWF98e2IcysOVnIfMVelmTKLMZJWgxBo0vCYId0z3OAbZdTqKucu_LwH8AAEB3AAAAAA|1|0|2c1b915272d875c107316839d17df84e21f0f240; _gat_UA-82424379-1=1; TAsessionID=93f89c97-fb5c-4002-88c9-56c3396541da|EXISTING; _gat_UA824243791=1; J27ARG5J; notice_behavior=implied,us; notice_gdpr_prefs=0,1,2:; notice_preferences=2:; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3; _uetsid=89298720bad911ef9169433d8ad3dbf7; _uetvid=f5cf396081e711efbc8b57485e8fde02; _ga=GA1.1.1290820127.1734262888; _ga_Q8JXK1T67J=GS1.1.1734262888.1.1.1734278145.0.0.0; _ga_VMTHZW7WSM=GS1.1.1734262887.1.1.1734278145.0.0.0",
    "if-none-match": 'W/"1208-MqladlVU7XZ7eajgILdFwpDI4eg"',
    "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjEzMDc1MTkiLCJhcCI6IjI0NTQ5MzA1IiwiaWQiOiJlMzAxNWE4YzUyYjg0YTNmIiwidHIiOiJlNzY1YTVhNTljOTlhMzZmNTY1YTA3ZjYxMDFhZTVkOSIsInRpIjoxNzM0Mjc4MTQ2MzA1LCJ0ayI6IjEzMDYzMTIifX0=",
    "priority": "u=1, i",
    "referer": "https://www.starbucks.com/menu/drinks/hot-coffees",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "traceparent": "00-e765a5a59c99a36f565a07f6101ae5d9-e3015a8c52b84a3f-01",
    "tracestate": "1306312@nr=0-1-1307519-24549305-e3015a8c52b84a3f----1734278146305",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

def get_stores(lat=None, lng=None, place=None):
    """
    Get a list of Starbucks stores based on latitude and longitude or a place name.

    Args:
    lat (float): The latitude of the location.
    long (float): The longitude of the location.
    place (str): The name of the place to search for.

    Returns:
    dict: The response data from the API.
    """

    end_point = "locations"
    params = {
        "lat": lat,
        "lng": lng,
        "place": place
    }
    url = os.path.join(base_url, end_point)
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data

def get_store_by_number(store_number):
    """
    Get a Starbucks store by its ID.

    Args:
    store_id (str): The ID of the store.

    Returns:
    dict: The response data from the API.
    """
    end_point = f"proxy/orchestra/get-store-by-number"
    data = {
        "variables": {
            "storeNumber": str(store_number)
        }
    }
    removable_keys = ['id']
    url = os.path.join(base_url, end_point)
    response = requests.post(url, headers=headers, json=data)
    data = response.json()
    remove_keys_recursively(data, removable_keys)
    return data
