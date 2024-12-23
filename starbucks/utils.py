import json
def remove_keys_recursively(data, keys_to_remove):
    """
    Removes all keys in `keys_to_remove` from a nested dictionary or list of dictionaries.

    Args:
    data (dict or list): The nested structure from which to remove keys.
    keys_to_remove (set): A set of keys to remove.

    Returns:
    None: Modifies the data in place.
    """
    if isinstance(data, dict):
        # Remove the keys at the current level
        for key in list(data.keys()):  # Use list to avoid runtime error while modifying dict
            if key in keys_to_remove:
                del data[key]
        # Recursively process the remaining values
        for key, value in data.items():
            remove_keys_recursively(value, keys_to_remove)
    elif isinstance(data, list):
        # If the value is a list, call the function for each item
        for item in data:
            remove_keys_recursively(item, keys_to_remove)


def search_for_key_value_recursively(data, key, value):
    """
    Searches for a key-value pair in a nested dictionary or list of dictionaries.

    Args:
    data (dict or list): The nested structure to search.
    key (str): The key to search for.
    value: The value to search for.

    Returns:
    dict: The first dictionary containing the key-value pair.
    """
    if isinstance(data, dict):
        # Check if the current dictionary contains the key-value pair
        if key in data and int(data[key]) == int(value):
            return data
        # Recursively search the values of the dictionary
        for sub_data in data.values():
            result = search_for_key_value_recursively(sub_data, key, value)
            if result is not None:
                return result
    elif isinstance(data, list):
        # If the value is a list, call the function for each item
        for item in data:
            result = search_for_key_value_recursively(item, key, value)
            if result is not None:
                return result
    return None

def get_product_uri_from_product_number(product_number):
    """
    Get the URI of a specific product by its product number.

    Args:
    product_number (str): The product number of the product.

    Returns:
    str: The URI of the product.
    """
        # use os path join to join the base_url and the endpoint
    # read json file
    with open('data/starbucks_menu.json') as f:
        data = json.load(f)
    product = search_for_key_value_recursively(data, "productNumber", product_number)
    if product is not None:
        return product["uri"]
    return None
