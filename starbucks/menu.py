import requests
from starbucks import base_url
from starbucks.utils import remove_keys_recursively, get_product_uri_from_product_number
import os

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
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
    url = '/'.join([base_url, endpoint])
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
    url = '/'.join([base_url, product_uri])
    print(url)
    params = {
        "storeNumber": store_number
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data