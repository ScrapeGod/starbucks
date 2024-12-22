import requests
from starbucks import base_url
from starbucks.utils import remove_keys_recursively, get_product_uri_from_product_number
import os

headers = {
    "accept": "application/json",
    "accept-language": "en-US",
    "cookie": "fp_token_7c6a6574-f011-4c9a-abdd-9894a102ccef=zDz3dkC5iUNiITh/WGqd/yT1CgLQOBBHD8160GQh36E=; optimizelyEndUserId=oeu1734262885695r0.9435912370295745; _gid=GA1.2.2090719523.1734262888; _gcl_au=1.1.1800411924.1734262888; ux_exp_id=58682600-9719-43dc-8ed2-c9b1e5c1348d; optimizelySession=0; _uetsid=89298720bad911ef9169433d8ad3dbf7; _uetvid=f5cf396081e711efbc8b57485e8fde02; _ga=GA1.2.1290820127.1734262888; _ga_VMTHZW7WSM=GS1.1.1734262887.1.1.1734280018.0.0.0; _ga_Q8JXK1T67J=GS1.1.1734262888.1.1.1734280116.0.0.0; tiWQK2tY=A06aH8qTAQAAdpROAMyWF98e2IcysOVnIfMVelmTKLMZJWgxBo0vCYId0z3OAbZdTqKucu_LwH8AAEB3AAAAAA|1|0|2c1b915272d875c107316839d17df84e21f0f240; TAsessionID=cf67aaa4-37cf-4a0c-b4ac-69efc1eb8207|EXISTING; notice_behavior=implied,us; yUsBm1Kz; notice_gdpr_prefs=0,1,2:; notice_preferences=2:; cmapi_gtm_bl=; cmapi_cookie_privacy=permit 1,2,3",
    "if-none-match": 'W/"1ee82-8q0TCiB2tvyLTHEzXknqKCqxHWw"',
    "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjEzMDc1MTkiLCJhcCI6IjI0NTQ5MzA1IiwiaWQiOiIyNzNmODQzNzkwZjgyYjg2IiwidHIiOiJhYjY1MmY0YjIwN2U5OTBhN2RmNjRhNjcyZmM2N2Y0NiIsInRpIjoxNzM0MzMwNDg0MzY3LCJ0ayI6IjEzMDYzMTIifX0=",
    "priority": "u=1, i",
    "referer": "https://www.starbucks.com/menu",
    "sec-ch-ua": '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "traceparent": "00-ab652f4b207e990a7df64a672fc67f46-273f843790f82b86-01",
    "tracestate": "1306312@nr=0-1-1307519-24549305-273f843790f82b86----1734330484367",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

def get_all_menu(store_number=None):
    """
    Get the full Starbucks menu.

    Returns:
    dict: The response data from the API.
    """
    params = {
        "storeNumber": store_number
    }
    removable_keys = ["displayOrder", "uri", "id"]
    # use os path join to join the base_url and the endpoint
    endpoint = "ordering/menu"
    url = os.path.join(base_url, endpoint)
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    # remove the keys that are not needed
    remove_keys_recursively(data, removable_keys)
    return data

def get_product_details(product_number, store_number=None):
    """
    Get the details of a specific product by its product number.

    Args:
    product_number (str): The product number of the product.

    Returns:
    dict: The response data from the API.
    """

    product_uri = get_product_uri_from_product_number(product_number)
    if product_uri:
        product_uri = product_uri.replace("/product", "ordering")
    url = os.path.join(base_url, product_uri)
    print(base_url, url, product_uri)
    params = {
        "storeNumber": store_number
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data